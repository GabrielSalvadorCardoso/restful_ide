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

from hyper_resource.models import FeatureCollectionModel

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

    # primitives
    int: {"@id": "https://schema.org/value", "@type": "https://schema.org/Integer"},
    bool:{"@id": "https://schema.org/value", "@type": "https://schema.org/Boolean"},
    str: {"@id": "https://schema.org/value", "@type": "https://schema.org/Text"},
    float: {"@id": "https://schema.org/value", "@type": "https://schema.org/Float"}
}

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
