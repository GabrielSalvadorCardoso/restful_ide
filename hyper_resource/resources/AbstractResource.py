from rest_framework.views import APIView
from rest_framework.negotiation import BaseContentNegotiation
from hyper_resource.contexts import AbstractContextResource
from rest_framework.response import Response
from rest_framework import status

CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, HEAD, OPTIONS",
    "Access-Control-Expose-Headers": "Link"
}
JSON_CONTENT_TYPE = "application/json"
CONTENT_TYPE_JSONLD = "application/ld+json"
OCTET_STREAM_CONTENT_TYPE = "application/octet-stream"

OPERATION_KWARGS_LABEL = "operation"
EXTENSION_KWARGS_LABEL = "extension"

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

    def get_operation_name_from_path(self, operation_snippet):
        return operation_snippet.split("/")[0]

    def add_cors_headers(self, response):
        for header, value in CORS_HEADERS.items():
            response[header] = value

    def default_content_types(self):
        return [JSON_CONTENT_TYPE, OCTET_STREAM_CONTENT_TYPE, CONTENT_TYPE_JSONLD]

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

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        self.add_cors_headers(response)
        return response

    def basic_get(self, request, *args, **kwargs):
        object = self.serializer_class.Meta.model.objects.get(pk=kwargs['pk'])
        serializer = self.serializer_class(object, context={'request': request})
        return RequiredObject(serializer.data, JSON_CONTENT_TYPE, 200)

    def options(self, request, *args, **kwargs):
        context = self.context_class().create_context_for_fields(self.serializer_class.Meta.model()._meta.fields)
        supported_property_context = self.context_class().get_supported_properties_for_fields(self.serializer_class.Meta.model()._meta.fields)
        context.update(supported_property_context)
        return Response(context, status=status.HTTP_200_OK, content_type=CONTENT_TYPE_JSONLD)