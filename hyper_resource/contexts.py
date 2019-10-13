"""
https://purl.org/geojson/vocab#FeatureCollection
https://purl.org/geojson/vocab#Feature
https://purl.org/geojson/vocab#Point
https://purl.org/geojson/vocab#LineString
https://purl.org/geojson/vocab#Polygon
https://purl.org/geojson/vocab#MultiPoint
https://purl.org/geojson/vocab#MultiLineString
https://purl.org/geojson/vocab#MultiPolygon
https://purl.org/geojson/vocab#GeometryCollection
https://purl.org/geojson/vocab#bbox
https://purl.org/geojson/vocab#coordinates
https://purl.org/geojson/vocab#features
https://purl.org/geojson/vocab#geometry
https://purl.org/geojson/vocab#id
https://purl.org/geojson/vocab#properties
https://purl.org/geojson/vocab#type
"""
from django.contrib.gis.geos import Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon, GEOSGeometry
from django.db.models import Q
from copy import deepcopy

from django.contrib.gis.db.models import GeometryCollectionField, GeometryField, PointField, LineStringField, \
    PolygonField, MultiPointField, MultiLineStringField, MultiPolygonField, FloatField
from django.db.models import AutoField, IntegerField, CharField, DecimalField

GEOMETRY_FIELD_NAMES = (GeometryField, PointField, LineStringField, PolygonField,
                        MultiPointField, MultiLineStringField, MultiPolygonField,
                        GeometryCollectionField)

from hyper_resource.models import FeatureCollectionModel, CollectionModel

VOCABULARY = {
    # todo: these IRIs references classes. The intent is to describe its instances (not his class), so these must be replaced. Like in BORBA (2017) uses http://ecoide.cos.urfj.br/instituicoes/ibge/contexts/geometry.jsonld
    # todo: search for "schema:rangeIncludes", "schema:domainIncludes", "schema:StructuredValue"
    # Geometrics
    GEOSGeometry: {"@id": "https://schema.org/value", "@type": "https://purl.org/geojson/vocab#geometry"},
    Point: {"@id": "https://schema.org/value", "@type": "https://purl.org/geojson/vocab#Point"},
    LineString: {"@id": "https://schema.org/value", "@type": "https://purl.org/geojson/vocab#LineString"},
    Polygon: {"@id": "https://schema.org/value", "@type": "https://purl.org/geojson/vocab#Polygon"},
    MultiPoint: {"@id": "https://schema.org/value", "@type": "https://purl.org/geojson/vocab#MultiPoint"},
    MultiLineString: {"@id": "https://schema.org/value", "@type": "https://purl.org/geojson/vocab#MultiLineString"},
    MultiPolygon: {"@id": "https://schema.org/value", "@type": "https://purl.org/geojson/vocab#MultiPolygon"},
    FeatureCollectionModel: {"@id": "https://schema.org/value", "@type": "https://purl.org/geojson/vocab#FeatureCollection"},
    Q: {"@id": "https://schema.org/query"},
    CollectionModel: {"@id": "https://schema.org/value", "@type": "http://www.w3.org/ns/hydra/core#Collection"},

    # primitives
    int: {"@id": "https://schema.org/value", "@type": "https://schema.org/Integer"},
    bool:{"@id": "https://schema.org/value", "@type": "https://schema.org/Boolean"},
    str: {"@id": "https://schema.org/value", "@type": "https://schema.org/Text"},
    float: {"@id": "https://schema.org/value", "@type": "https://schema.org/Float"}
}

class AbstractContextResource(object):
    # todo: search by PyLD features - https://github.com/digitalbazaar/pyld
    def get_term_definition_dict(self):
        term_definition_dict = {
            "name":         "https://schema.org/name",
            AutoField:      "https://schema.org/propertyID",
            IntegerField:   {"@id": "https://schema.org/value", "@type": "https://schema.org/Integer"},
            CharField:      {"@id": "https://schema.org/value", "@type": "https://schema.org/Text"},
            DecimalField:   {"@id": "https://schema.org/value", "@type": "https://schema.org/Float"},
            FloatField: {"@id": "https://schema.org/value", "@type": "https://schema.org/Float"},
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

    def get_supported_properties_for_fields(self, fields):
        supported_propeties = {"hydra:supportedProperty": []}
        for field in fields:
            supported_propeties["hydra:supportedProperty"].append({
                "hydra:property": field.name,
                "hydra:writable": not field.primary_key and field.editable,
                "hydra:readable": True,
                "hydra:required": not field.null
            })
        return supported_propeties

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
        fields_no_geom = []
        for field in fields:
            if self.is_geometry_field(field):
                continue

            if field.primary_key:
                field.name = "id"
            fields_no_geom.append(field)
        #fields_no_geom = [field for field in fields if not self.is_geometry_field(field)]

        return super().create_context_for_fields(fields_no_geom)

    def create_context_for_operations(self, operations_dict):
        supperted_operation_dict = {"hydra:supportedOperation": []}
        for name, operation in operations_dict.items():
            supperted_operation_dict["hydra:supportedOperation"].append(operation.get_hydra_description())
        return supperted_operation_dict

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

# ------------------- Operations Context -------------------
class OperationContext(object):
    def get_context(self, operation):
        expects = [VOCABULARY[param_type] for param_type in operation.parameters_types]
        returns = VOCABULARY[operation.return_type]

        return {
            "hydra:title": operation.name,
            "hydra:method": "GET",
            "hydra:statusCode": [200],
            "@type": "hydra:Operation",
            "hydra:expects": expects,
            "hydra:returns": returns
        }
