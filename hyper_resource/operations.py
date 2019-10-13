import json

import requests
from django.contrib.gis.geos import Polygon, GEOSGeometry, MultiPolygon, MultiLineString, MultiPoint, LineString, Point, \
    GEOSException
from django.db.models import Q

from hyper_resource.contexts import OperationContext
from hyper_resource.models import FeatureModel, FeatureCollectionModel, CollectionModel


class TooMuchParametersError(Exception):
    pass

class WrongParameterTypeError(Exception):
    pass

class InvalidOperationException(Exception):
    pass

PARAM_SEPARATOR = "&"


class Operation(object):
    name = "operation" # must be overided
    return_type = object # must be overided
    parameters_types = [] # must be overided
    context = OperationContext()

    def get_remaining_operations_snippet(self, parameters_str):
        # parameters_str.split("/")[0] == operation_name | parameters_str.split("/")[1] == operations_parameters
        return "/".join(parameters_str.split("/")[2:])

    def convert_parameters(self, parameters_str):
        raise NotImplementedError("set_parameters must be implemented")

    def get_hydra_description(self):
        return self.context.get_context(self)

class SpatialOperation(Operation):
    pass

class Area(SpatialOperation):
    name = "area"
    return_type = float
    parameters_types = []

    def get_remaining_operations_snippet(self, parameters_str):
        return "/".join(parameters_str.split("/")[1:])

    def convert_parameters(self, parameters_str):
        return None

class Buffer(SpatialOperation):
    name = "buffer"
    return_type = GEOSGeometry
    parameters_types = [float, int]

    def get_remaining_operations_snippet(self, parameters_str):
        return "/".join(parameters_str.split("/")[2:])

    def convert_parameters(self, parameters_str):
        try:
            operation_name, params = parameters_str.split("/")[0], parameters_str.split("/")[1].split(PARAM_SEPARATOR)
            if len(params) > 1:
                return (float(params[0]), int(params[1]))
            else:
                return (float(params[0]), 8) # parameter clone default is False
        except ValueError:
            raise WrongParameterTypeError

class Envelope(SpatialOperation):
    """
    params: None
    """
    name = "envelope"
    return_type = Polygon
    parameters_types = []

    def get_remaining_operations_snippet(self, parameters_str):
        return "/".join(parameters_str.split("/")[1:])

    def convert_parameters(self, parameters_str):
        return None
        #raise TooMuchParametersError("This operation expected no arguments")

class Tranform(SpatialOperation):
    """
    params: ct, clone=False
    """
    name = "transform"
    return_type = GEOSGeometry
    parameters_types = [int]

    def convert_parameters(self, parameters_str):
        try:
            operation_name, params = parameters_str.split("/")[0], parameters_str.split("/")[1].split(PARAM_SEPARATOR)
            if len(params) > 1:
                return (int(params[0]), bool(params[1]))
            else:
                return (int(params[0]), True) # parameter clone default is False
        except ValueError:
            raise WrongParameterTypeError


class CollectionOperation(Operation):
    pass

class Filter(CollectionOperation):
    name = "filter"
    return_type = CollectionModel
    parameters_types = [Q]
    context = OperationContext()

    def convert_to_expression(self, parameters_str):
        d = {
            "eq": self.q_object_equals
        }
        operator = parameters_str.split("/")[2]
        return d[operator](parameters_str)

    # todo: convert value after 'eq' operator to same attribute type before 'eq' operator
    def q_object_equals(self, parameters_str):
        attribute_name = parameters_str.split("/")[1]
        value = parameters_str.split("/")[3]
        d = {attribute_name: value}
        return Q(**d)

    # todo: not implemented yet
    def convert_parameters(self, parameters_str):
        return (self.convert_to_expression(parameters_str),)

class FeatureCollectionOperation(CollectionOperation):
    pass

class SpatialFilterOperation(FeatureCollectionOperation):
    def is_uri(self, operation_snippet):
        return operation_snippet.startswith("http://") or\
               operation_snippet.startswith("httpz://") or\
               operation_snippet.startswith("www.")

    def get_remaining_operations_snippet(self, parameters_str):
        # todo: create regex to cut inner URI
        return "/".join(parameters_str.split("/")[1:])

    def convert_parameters(self, parameters_str):
        try:
            param = "/".join(parameters_str.split("/")[1:])
            return GEOSGeometry(param)
        except GEOSException:
            raise WrongParameterTypeError
        except ValueError:
            param = "/".join(parameters_str.split("/")[1:])
            if self.is_uri(param):
                response = requests.get(param)
                return GEOSGeometry(json.dumps(json.loads(response.text)["geometry"]))
            raise WrongParameterTypeError

class Crosses(SpatialFilterOperation):
    name = "crosses"
    return_type = FeatureCollectionModel
    parameters_types = [GEOSGeometry]
    context = OperationContext()

class Within(SpatialFilterOperation):
    name = "within"
    return_type = FeatureCollectionModel
    parameters_types = [GEOSGeometry]
    context = OperationContext()

SPATIAL_OPERATIONS = {
    Envelope.name: Envelope(),
    Tranform.name: Tranform(),
    Buffer.name: Buffer(),
    Area.name: Area()
}

FEATURE_COLLECTION_OPERATIONS = {
    Filter.name: Filter(), # todo: must be in superclass
    Within.name: Within(),
    Crosses.name: Crosses()
}

OPERATIONS_BY_TYPE = {
    FeatureModel: SPATIAL_OPERATIONS,
    GEOSGeometry: SPATIAL_OPERATIONS,
    Point: SPATIAL_OPERATIONS,
    LineString: SPATIAL_OPERATIONS,
    Polygon: SPATIAL_OPERATIONS,
    MultiPoint: SPATIAL_OPERATIONS,
    MultiLineString: SPATIAL_OPERATIONS,
    MultiPolygon: SPATIAL_OPERATIONS,

    FeatureCollectionModel: FEATURE_COLLECTION_OPERATIONS
}