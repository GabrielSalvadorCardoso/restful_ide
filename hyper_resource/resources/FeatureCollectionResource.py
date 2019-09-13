import json

from django.contrib.gis.geos import GeometryCollection, GEOSGeometry
from django.db.models import QuerySet
from django.http import HttpResponse
from rest_framework.response import Response

from bcim.contexts import FeatureCollectionContextResource
from hyper_resource import operations
from hyper_resource.models import FeatureCollectionModel, FeatureModel
from hyper_resource.operations import InvalidOperationException
from hyper_resource.resources.AbstractCollectionResource import AbstractCollectionResource
from hyper_resource.resources.AbstractResource import RequiredObject, JSON_CONTENT_TYPE, \
    NoAvailableRepresentationException
from hyper_resource.resources.FeatureUtils import FeatureUtils, CONTENT_TYPE_GEOJSON, CONTENT_TYPE_IMAGE_PNG


class FeatureCollectionResource(AbstractCollectionResource):
    context_class = FeatureCollectionContextResource

    def __init__(self):
        super().__init__()
        self.feature_utils = FeatureUtils()

    def generate_geometry_collection(self, queryset):
        geometries = []

        srid = None
        for idx, feature in enumerate(queryset):
            if idx == 0:
                srid = feature.geom.srs.srid
            geometries.append(feature.geom)

        return GeometryCollection(*geometries, srid=srid)

    # ------------------- content type decider methods -------------------

    def available_content_types_for_type(self, object_type):
        d = {
            FeatureCollectionModel: self.feature_utils.default_content_types(),
            QuerySet: self.feature_utils.default_content_types()
        }
        try:
            return d[object_type]
        except KeyError:
            raise NoAvailableRepresentationException("There's no available representations for this resource type: " + object_type)

    def content_type_for_object_type(self, request, object_type):
        contype_accept = self.feature_utils.content_type_by_accept(request)
        contype_obj_type = self.available_content_types_for_type(object_type)
        if contype_accept in contype_obj_type:
            return contype_accept
        return self.default_content_type_for_type(object_type)

    def default_content_type_for_type(self, object_type):
        if issubclass(object_type, QuerySet) or issubclass(object_type, GEOSGeometry):
            return CONTENT_TYPE_GEOJSON
        raise NoAvailableRepresentationException(
            "There's no available representations for this resource type: " + object_type)

    # ------------------- operation methods -------------------

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
                fcm_instance = FeatureCollectionModel()
                return getattr(fcm_instance, operation_name)(self.serializer_class.Meta.model, parameters_converted[0])
                #operation_result = getattr(FeatureCollectionModel(), operation_name)(*parameters_converted)
                #return operation_result
        else:
            raise InvalidOperationException(operation_snippet + " isn't a valid operation")

        #rem_oper_snippert = operation.get_remaining_operations_snippet(operation_snippet)
        #if rem_oper_snippert:
        #    return self.execute_operation(operation_result, rem_oper_snippert)
        #return operation_result

    def is_operation_for_type(self, operation_name, object_type):
        try:
            object_type = FeatureCollectionModel if issubclass(object_type, FeatureModel) else object_type
            operations_for_object_type = operations.OPERATIONS_BY_TYPE[object_type]
            return operation_name in operations_for_object_type
        except KeyError:
            return False

    def get_operation_for_type(self, operation_name, object_type):
        try:
            object_type = FeatureCollectionModel if issubclass(object_type, FeatureModel) else object_type
            operations_for_object_type = operations.OPERATIONS_BY_TYPE[object_type]
            return operations_for_object_type[operation_name]
        except KeyError:
            raise InvalidOperationException(operation_name + " isn't an operation for " + object_type)

    # ------------------- GET response methods -------------------

    def basic_get(self, request, *args, **kwargs):
        empty_object = self.serializer_class.Meta.model()
        if "operation" in kwargs:
            return self.required_object_for_operation(request, empty_object, *args, **kwargs)

        queryset = self.serializer_class.Meta.model.objects.all()
        contype_accept = self.feature_utils.content_type_by_accept(request, *args, kwargs)
        serialize_data = self.serialize_object(request, queryset, contype_accept)
        return RequiredObject(serialize_data, contype_accept, 200)

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
            operation_result = self.execute_operation(object, kwargs["operation"])
            contype_type = self.content_type_for_object_type(request, type(operation_result))
            serialize_data = self.serialize_object(request, operation_result, contype_type)
            return RequiredObject(serialize_data, contype_type, 200)

        except InvalidOperationException as ex:
            return RequiredObject(
                json.dumps( {"Invalid Operation": ex.args[0]} ),
                JSON_CONTENT_TYPE, 400
            )

    # ------------------- serializer methods -------------------

    def serialize_object(self, request, objects, content_type):

        if content_type == CONTENT_TYPE_IMAGE_PNG:
            if isinstance(objects, QuerySet):
                geometry_collection = self.generate_geometry_collection(objects)
                return self.feature_utils.generate_geometric_image(geometry_collection)
            return self.feature_utils.generate_geometric_image(objects)

        if isinstance(objects, QuerySet):
            return self.serializer_class(objects, context={'request': request}, many=True).data
        return json.loads(objects)