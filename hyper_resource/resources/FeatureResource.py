import json

from django.contrib.gis.geos import GEOSGeometry, Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from bcim.contexts import FeatureContextResource
from hyper_resource import operations
from hyper_resource.models import FeatureModel
from hyper_resource.operations import InvalidOperationException
from hyper_resource.resources.AbstractResource import AbstractResource, RequiredObject, JSON_CONTENT_TYPE, \
    CONTENT_TYPE_JSONLD, NoAvailableRepresentationException
from hyper_resource.resources.FeatureUtils import FeatureUtils, CONTENT_TYPE_GEOJSON, CONTENT_TYPE_IMAGE_PNG


class FeatureResource(AbstractResource):
    context_class = FeatureContextResource

    def __init__(self):
        super().__init__()
        self.feature_utils = FeatureUtils()

    # ------------------- content type decider methods -------------------

    def available_content_types_for_type(self, object_type):
        d = {
            FeatureModel: self.feature_utils.default_content_types(),
            Point: self.feature_utils.default_content_types(),
            LineString: self.feature_utils.default_content_types(),
            Polygon: self.feature_utils.default_content_types(),
            MultiPoint: self.feature_utils.default_content_types(),
            MultiLineString: self.feature_utils.default_content_types(),
            MultiPolygon: self.feature_utils.default_content_types()
        }
        try:
            return d[object_type]
        except KeyError:
            raise NoAvailableRepresentationException("There's no available representations for this resource type: " + object_type)

    def default_content_type_for_type(self, object_type):
        if issubclass(object_type, FeatureModel) or issubclass(object_type, GEOSGeometry):
            return CONTENT_TYPE_GEOJSON
        raise NoAvailableRepresentationException(
            "There's no available representations for this resource type: " + object_type)

    def content_type_for_object_type(self, request, object_type):
        contype_accept = self.feature_utils.content_type_by_accept(request)
        contype_obj_type = self.available_content_types_for_type(object_type)
        if contype_accept in contype_obj_type:
            return contype_accept
        return self.default_content_type_for_type(object_type)

    # ------------------- OPTIONS response methods -------------------

    def options(self, request, *args, **kwargs):
        required_object = self.basic_options(request, *args, **kwargs)
        return Response(
            required_object.representation_object,
            status=required_object.status_code,
            content_type=required_object.content_type
        )

    def basic_options(self, request, *args, **kwargs):
        if "operation" in kwargs:
            return self.required_context_for_operation(request, *args, **kwargs)
        return self.base_required_context(request, *args, **kwargs)

    def base_required_context(self, request, *args, **kwargs):
        context = {}
        term_definition_context = self.context_class().create_context_for_fields(self.serializer_class.Meta.model()._meta.fields)
        supported_operation_context = self.context_class().create_context_for_operations(operations.OPERATIONS_BY_TYPE[FeatureModel])

        context.update(term_definition_context)
        context.update(supported_operation_context)

        return RequiredObject(context, CONTENT_TYPE_JSONLD, 200)

    def required_context_for_operation(self, request, *args, **kwargs):
        context = {}
        operation_return_type = self.get_operation_return_type(kwargs["operation"])
        supported_operation_context = self.context_class().create_context_for_operations(operations.OPERATIONS_BY_TYPE[operation_return_type])
        context.update(supported_operation_context)
        return RequiredObject(context, CONTENT_TYPE_JSONLD, 200)

    # ------------------- operation methods -------------------

    def get_operation_return_type(self, operation_snippet, current_return_type=FeatureModel):
        operation_name = self.get_operation_name_from_path(operation_snippet)

        if self.is_operation_for_type(operation_name, current_return_type):
            operation = self.get_operation_for_type(operation_name, current_return_type)
        else:
            raise InvalidOperationException(operation_snippet + " isn't a valid operation")

        rem_oper_snippert = operation.get_remaining_operations_snippet(operation_snippet)
        if rem_oper_snippert:
            return self.get_operation_return_type(rem_oper_snippert, current_return_type=operation.return_type)
        return operation.return_type

    def get_operation_for_type(self, operation_name, object_type):
        try:
            object_type = FeatureModel if issubclass(object_type, FeatureModel) else object_type
            operations_for_object_type = operations.OPERATIONS_BY_TYPE[object_type]
            return operations_for_object_type[operation_name]
        except KeyError:
            raise InvalidOperationException(operation_name + " isn't an operation for " + object_type)

    # todo: move to hyper_resource.operations
    def execute_operation(self, object, operation_snippet):
        operation_name = self.get_operation_name_from_path(operation_snippet)
        if self.is_operation_for_type(operation_name, type(object)):
            operation = self.get_operation_for_type(operation_name, type(object))
            parameters_converted = operation.convert_parameters(operation_snippet)
            if parameters_converted == None:
                try:
                    operation_result = getattr(object, operation_name)()
                except TypeError:
                    operation_result = getattr(object, operation_name)
            else:
                operation_result = getattr(object, operation_name)(*parameters_converted)
        else:
            raise InvalidOperationException(operation_snippet + " isn't a valid operation")

        rem_oper_snippert = operation.get_remaining_operations_snippet(operation_snippet)
        if rem_oper_snippert:
            return self.execute_operation(operation_result, rem_oper_snippert)
        return operation_result

    def is_operation_for_type(self, operation_name, object_type):
        try:
            object_type = FeatureModel if issubclass(object_type, FeatureModel) else object_type
            operations_for_object_type = operations.OPERATIONS_BY_TYPE[object_type]
            return operation_name in operations_for_object_type
        except KeyError:
            return False

    # ------------------- GET response methods -------------------

    def get(self, request, *args, **kwargs):
        required_object = self.basic_get(request, *args, **kwargs)

        if required_object.content_type == CONTENT_TYPE_IMAGE_PNG:
            return HttpResponse(
                required_object.representation_object,
                status=required_object.status_code,
                content_type=CONTENT_TYPE_IMAGE_PNG
            )

        return Response(
            required_object.representation_object,
            status=required_object.status_code,
            content_type=CONTENT_TYPE_GEOJSON
        )

    def required_object_for_operation(self, request, object, *args, **kwargs):
        try:
            # todo: need to decide content-type (by operation return type and accept) and serialization
            operation_result = self.execute_operation(object, kwargs["operation"])
            contype_type = self.content_type_for_object_type(request, type(operation_result))
            serialize_data = self.serialize_object(request, operation_result, contype_type)
            return RequiredObject(serialize_data, contype_type, 200)

        except InvalidOperationException as ex:
            return RequiredObject(
                json.dumps( {"Invalid Operation": ex.args[0]} ),
                JSON_CONTENT_TYPE, 400
            )

    def basic_get(self, request, *args, **kwargs):
        pk_dict = {}
        pk_dict["pk"] = kwargs["pk"]
        object = get_object_or_404(self.serializer_class.Meta.model, **pk_dict)

        # http://192.168.0.11:8000/api/restfull-ide/bcim/unidades-federativas/1/envelope/transform/3857/envelope/transform/3674
        if "operation" in kwargs:
            return self.required_object_for_operation(request, object, *args, **kwargs)

        contype_accept = self.feature_utils.content_type_by_accept(request, *args, kwargs)
        serialize_data = self.serialize_object(request, object, contype_accept)
        return RequiredObject(serialize_data, contype_accept, 200)

    # ------------------- serializer methods -------------------

    def serialize_object(self, request, object, content_type):
        if content_type == CONTENT_TYPE_IMAGE_PNG:
            if isinstance(object, FeatureModel):
                return self.feature_utils.generate_geometric_image(object.geom)
            return self.feature_utils.generate_geometric_image(object)

        if isinstance(object, FeatureModel):
            return self.serializer_class(object, context={'request': request}).data
        if isinstance(object, GEOSGeometry):
            return json.loads(object.geojson)
        return json.loads(object)
