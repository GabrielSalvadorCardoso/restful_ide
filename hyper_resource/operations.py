import json

import requests
from django.contrib.gis.geos import Polygon, GEOSGeometry, MultiPolygon, MultiLineString, MultiPoint, LineString, Point, \
    GEOSException

from hyper_resource.context import OperationContext
from hyper_resource.models import FeatureModel, FeatureCollectionModel


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


class FeatureCollectionOperation(Operation):
    pass

class Within(FeatureCollectionOperation):
    name = "within"
    return_type = FeatureCollectionModel
    parameters_types = [GEOSGeometry]
    context = OperationContext()

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

SPATIAL_OPERATIONS = {
    Envelope.name: Envelope(),
    Tranform.name: Tranform()
}

FEATURE_COLLECTION_OPERATIONS = {
    Within.name: Within()
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