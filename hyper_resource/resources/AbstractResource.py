import json

from rest_framework.views import APIView
from rest_framework.negotiation import BaseContentNegotiation

from hyper_resource import operations
from hyper_resource.contexts import AbstractContextResource
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, HEAD, OPTIONS",
    "Access-Control-Expose-Headers": "Link"
}
JSON_CONTENT_TYPE = "application/json"
CONTENT_TYPE_JSONLD = "application/ld+json"
OCTET_STREAM_CONTENT_TYPE = "application/octet-stream"

OPERATION_OR_ATTRIBUTES_KWARGS_LABEL = "operation_or_attributes"
EXTENSION_KWARGS_LABEL = "extension"

ATTRIBUTES_SEPARATOR = ","

class NoAvailableRepresentationException(Exception):
    pass

class RequiredObject(object):
    def __init__(self, representation_object, content_type, status_code, etag=None):
        self.representation_object = representation_object
        self.content_type = content_type
        self.status_code = status_code
        self.etag = etag

class BlankContentNegotiation(BaseContentNegotiation):
    '''
    Class to ignore django rest framework default renders
    '''
    def select_parser(self, request, parsers):
        return parsers[0]

    def select_renderer(self, request, renderers, format_suffix=None):
        return (renderers[0], renderers[0].media_type)

class AbstractResource(APIView):
    content_negotiation_class = BlankContentNegotiation
    serializer_class = None
    context_class = AbstractContextResource

    # ------------------- path analysis methods -------------------
    def get_operation_name_from_path(self, operation_snippet):
        return operation_snippet.split("/")[0]

    def remove_last_slash(self, path):
        return path if path[-1] != "/" else path[:-1]

    def path_has_only_attributes(self, kwargs):
        try:
            path = self.remove_last_slash( kwargs[OPERATION_OR_ATTRIBUTES_KWARGS_LABEL] )
            path_arr = path.split("/")

            if len(path_arr) > 1:
                return False

            attributes = path_arr[0].split(ATTRIBUTES_SEPARATOR)
            for attr in attributes:
                if attr not in self.serializer_class.Meta.fields:
                    return False
            return True

        except KeyError:
            return False

    # ------------------- operation methods -------------------
    def get_operation_return_type(self, operation_snippet, current_return_type=object):
        raise NotImplementedError("'get_operation_return_type' must be implemented")

    def add_cors_headers(self, response):
        for header, value in CORS_HEADERS.items():
            response[header] = value

    # ------------------- content type decider methods -------------------
    def content_type_by_accept(self, request, *args, **kwargs):
        if request.META['HTTP_ACCEPT'] in self.default_content_types():
            return request.META['HTTP_ACCEPT']

        return JSON_CONTENT_TYPE

    def default_content_types(self):
        return [JSON_CONTENT_TYPE, OCTET_STREAM_CONTENT_TYPE, CONTENT_TYPE_JSONLD]

    def content_type_for_attributes(self, request, attributes_dict, *args, **kwargs):
        contype_accept = self.content_type_by_accept(request)
        if contype_accept in self.default_content_types():
            return contype_accept
        return JSON_CONTENT_TYPE

    def available_content_types_for_type(self, object_type):
        d = {
            float: self.default_content_types(),
            int: self.default_content_types(),
            str: self.default_content_types(),
            bool: self.default_content_types(),
        }
        try:
            return d[object_type]
        except KeyError:
            raise NoAvailableRepresentationException("There's no available representations for this resource type: " + object_type)

    def default_content_type_for_type(self, object_type):
        return JSON_CONTENT_TYPE
        #raise NoAvailableRepresentationException(
        #    "There's no available representations for this resource type: " + object_type)

    def get_object_query_dict(self, **kwargs):
        pk_dict = {}
        pk_dict["pk"] = kwargs["pk"]
        return pk_dict

    def get_object(self, **kwargs):
        query_dict = self.get_object_query_dict(**kwargs)
        return get_object_or_404(self.serializer_class.Meta.model, **query_dict)

    def get_objects_for_attributes(self, request, *args, **kwargs):
        query_dict = self.get_object_query_dict(**kwargs)
        attribute_arr = kwargs[OPERATION_OR_ATTRIBUTES_KWARGS_LABEL].split(ATTRIBUTES_SEPARATOR)
        return self.serializer_class.Meta.model.objects.filter(**query_dict).values(*attribute_arr).first()

    def required_object_for_attributes(self, request, *args, **kwargs):
        attributes_dict = self.get_objects_for_attributes(request, *args, **kwargs)
        contype_type = self.content_type_for_attributes(request, attributes_dict, *args, **kwargs)
        serialized_data = self.serialize_object_for_attributes(request, attributes_dict, contype_type)
        return RequiredObject(serialized_data, contype_type, 200)

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        self.add_cors_headers(response)
        return response

    def get(self, request, *args, **kwargs):
        required_object = self.basic_get(request, *args, **kwargs)
        return Response(
            required_object.representation_object,
            status=required_object.status_code,
            content_type=JSON_CONTENT_TYPE
        )

    def basic_get(self, request, *args, **kwargs):
        if self.path_has_only_attributes(kwargs):
            return self.required_object_for_attributes(request, *args, **kwargs)

        #object = self.serializer_class.Meta.model.objects.get(pk=kwargs['pk'])
        object = self.get_object(**kwargs)

        contype_accept = self.content_type_by_accept(request, *args, kwargs)
        serializer = self.serializer_class(object, context={'request': request})
        return RequiredObject(serializer.data, contype_accept, 200)

    # ------------------- OPTIONS response methods -------------------
    def base_required_context(self, request, *args, **kwargs):
        context = {}
        term_definition_context = self.context_class().create_context_for_fields(self.serializer_class.Meta.model()._meta.fields)
        #supported_operation_context = self.context_class().create_context_for_operations(operations.OPERATIONS_BY_TYPE[FeatureModel])
        supported_properties_context = self.context_class().get_supported_properties_for_fields(self.serializer_class.Meta.model()._meta.fields)

        context.update(supported_properties_context)
        context.update(term_definition_context)
        #context.update(supported_operation_context)

        return RequiredObject(context, CONTENT_TYPE_JSONLD, 200)

    def required_context_for_attributes(self, request, *args, **kwargs):
        context = {}
        attribute_arr = kwargs[OPERATION_OR_ATTRIBUTES_KWARGS_LABEL].split(ATTRIBUTES_SEPARATOR)
        fields = []

        model_field_names = [field.name for field in self.serializer_class.Meta.model()._meta.fields]
        for attribute in attribute_arr:
            if attribute in model_field_names:
                for field in self.serializer_class.Meta.model()._meta.fields:
                    if field.name == attribute:
                        fields.append(field)
                        break

        term_definition_context = self.context_class().create_context_for_fields(fields)
        context.update(term_definition_context)

        return RequiredObject(context, CONTENT_TYPE_JSONLD, 200)

    def required_context_for_operation(self, request, *args, **kwargs):
        context = {}
        operation_return_type = self.get_operation_return_type(kwargs[OPERATION_OR_ATTRIBUTES_KWARGS_LABEL])
        try:
            supported_operation_context = self.context_class().create_context_for_operations(operations.OPERATIONS_BY_TYPE[operation_return_type])
        except KeyError:
            supported_operation_context = {"hydra:supportedOperation": []}
        context.update(supported_operation_context)
        return RequiredObject(context, CONTENT_TYPE_JSONLD, 200)

    def options(self, request, *args, **kwargs):
        required_object = self.basic_options(request, *args, **kwargs)
        return Response(
            required_object.representation_object,
            status=required_object.status_code,
            content_type=required_object.content_type
        )

    def basic_options(self, request, *args, **kwargs):
        if self.path_has_only_attributes(kwargs):
            return self.required_context_for_attributes(request, *args, **kwargs)

        if OPERATION_OR_ATTRIBUTES_KWARGS_LABEL in kwargs:
            return self.required_context_for_operation(request, *args, **kwargs)
        return self.base_required_context(request, *args, **kwargs)

    # ------------------- serializer methods -------------------
    def serialize_object_for_attributes(self, request, attributes_dict, content_type):
        return attributes_dict