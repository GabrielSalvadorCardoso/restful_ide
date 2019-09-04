from django.contrib.gis.geos import Polygon

from hyper_resource.models import FeatureModel

class TooMuchParametersError(Exception):
    pass

class WrongParameterTypeError(Exception):
    pass

class InvalidOperationException(Exception):
    pass

PARAM_SEPARATOR = "&"

class Operation(object):
    def get_remaining_operations_snippet(self, parameters_str):
        # parameters_str.split("/")[0] == operation_name | parameters_str.split("/")[1] == operations_parameters
        return "/".join(parameters_str.split("/")[2:])

    def convert_parameters(self, parameters_str):
        raise NotImplementedError("set_parameters must be implemented")

class SpatialOperation(Operation):
    pass

class Envelope(SpatialOperation):
    """
    params: None
    """
    name = "envelope"
    return_type = Polygon

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

    def convert_parameters(self, parameters_str):
        try:
            operation_name, params = parameters_str.split("/")[0], parameters_str.split("/")[1].split(PARAM_SEPARATOR)
            if len(params) > 1:
                return (int(params[0]), bool(params[1]))
            else:
                return (int(params[0]), True) # parameter clone default is False
        except ValueError:
            raise WrongParameterTypeError

SPATIAL_OPERATIONS = {
    Envelope.name: Envelope(),
    Tranform.name: Tranform()
}

OPERATIONS_BY_TYPE = {
    FeatureModel: SPATIAL_OPERATIONS,
    Polygon: SPATIAL_OPERATIONS
}

def is_operation_for_type(operation_name, object_type):
    try:
        object_type = FeatureModel if issubclass(object_type, FeatureModel) else object_type
        operations_for_object_type = OPERATIONS_BY_TYPE[object_type]
        return operation_name in operations_for_object_type
    except KeyError:
        return False

def get_operation_for_type(operation_name, object_type):
    try:
        object_type = FeatureModel if issubclass(object_type, FeatureModel) else object_type
        operations_for_object_type = OPERATIONS_BY_TYPE[object_type]
        return operations_for_object_type[operation_name]
    except KeyError:
        raise InvalidOperationException(operation_name + " isn't an operation for " + object_type)