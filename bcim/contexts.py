from copy import deepcopy

from django.contrib.gis.db.models import GeometryCollectionField, GeometryField, PointField, LineStringField, PolygonField, MultiPointField, MultiLineStringField, MultiPolygonField
from django.db.models import AutoField, IntegerField, CharField

GEOMETRY_FIELD_NAMES = (GeometryField, PointField, LineStringField, PolygonField,
                        MultiPointField, MultiLineStringField, MultiPolygonField,
                        GeometryCollectionField)

class AbstractContextResource(object):
    # todo: search by PyLD features - https://github.com/digitalbazaar/pyld
    def get_term_definition_dict(self):
        term_definition_dict = {
            "name":         "https://schema.org/name",
            AutoField:      "https://schema.org/propertyID",
            IntegerField:   {"@id": "https://schema.org/value", "@type": "https://schema.org/Integer"},
            CharField:      {"@id": "https://schema.org/value", "@type": "https://schema.org/Text"},
        }
        return deepcopy(term_definition_dict)

    def create_context_for_fields(self, fields):
        context_dict = {"@context": {}}

        for field in fields:
            try:
                context_dict["@context"].update({
                    field.name: self.get_term_definition_dict()[field.name]
                })
            except KeyError:
                context_dict["@context"].update({
                    field.name: self.get_term_definition_dict()[type(field)]
                })
        return context_dict

class AbstractCollectionContextResource(AbstractContextResource):
    pass

class FeatureCollectionContextResource(AbstractCollectionContextResource):

    # todo: must implement GeoJson terms definition
    def get_term_definition_dict(self):
        term_definition_dict = super().get_term_definition_dict()
        term_definition_dict.update({})
        return deepcopy(term_definition_dict)

    def is_geometry_field(self, field):
        return type(field) in GEOMETRY_FIELD_NAMES

    def create_context_for_fields(self, fields):
        fields_no_geom = [field for field in fields if not self.is_geometry_field(field)]
        return super().create_context_for_fields(fields_no_geom)

class FeatureContextResource(AbstractContextResource):
    # todo: must implement GeoJson terms definition
    # todo: refactoring: this method is a copy and paste of the FeatureCollectionContextResource class
    def get_term_definition_dict(self):
        term_definition_dict = super().get_term_definition_dict()
        term_definition_dict.update({})
        return deepcopy(term_definition_dict)

    # todo: refactoring: this method is a copy and paste of the FeatureCollectionContextResource class
    def is_geometry_field(self, field):
        return type(field) in GEOMETRY_FIELD_NAMES

    # todo: refactoring: this method is a copy and paste of the FeatureCollectionContextResource class
    def create_context_for_fields(self, fields):
        fields_no_geom = [field for field in fields if not self.is_geometry_field(field)]
        return super().create_context_for_fields(fields_no_geom)

    def create_context_for_operations(self, operations_dict):
        supperted_operation_dict = {"hydra:supportedOperation": []}
        for name, operation in operations_dict.items():
            supperted_operation_dict["hydra:supportedOperation"].append(operation.get_hydra_description())
        return supperted_operation_dict
