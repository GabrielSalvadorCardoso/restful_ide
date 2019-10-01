import os

import mapnik
from django.http import HttpResponse
from rest_framework.response import Response

from hyper_resource.models import FeatureModel
from hyper_resource.resources.AbstractResource import AbstractResource, CONTENT_TYPE_JSONLD, \
    NoAvailableRepresentationException
from django.contrib.gis.geos import Point, LineString, Polygon, MultiPoint, MultiPolygon, MultiLineString, GEOSGeometry
CONTENT_TYPE_GEOJSON = "application/geo+json"
CONTENT_TYPE_IMAGE_PNG = "image/png"

class FeatureUtils(AbstractResource):
    """
    This isn't a Hyper Resource class. The role pf this class is to
    concentrate behavior common to FeatureResource and FeatureCollectionResource
    """
    def default_content_types(self):
        return [CONTENT_TYPE_IMAGE_PNG, CONTENT_TYPE_GEOJSON, CONTENT_TYPE_JSONLD]

    def content_type_by_accept(self, request, *args, **kwargs):
        if request.META['HTTP_ACCEPT'] in self.default_content_types():
            return request.META['HTTP_ACCEPT']

        try:
            if 'extension' in args[0] and args[0]['extension'] == '.png':
                return CONTENT_TYPE_IMAGE_PNG
        except IndexError:
            return CONTENT_TYPE_GEOJSON

        return CONTENT_TYPE_GEOJSON

    def define_geometry_collection_type(self, geometry_collection):
        geometries_types = []
        for geometry in geometry_collection:
            if not geometry.geom_type in geometries_types:
                geometries_types.append(geometry.geom_type)
            if len(geometries_types) > 2:
                return geometry_collection.geom_type

        if len(geometries_types) == 1: # all geometries has the same time
            return geometries_types[0]
        elif len(geometries_types) == 2:
            # Point and MultiPoint or Polygon and MultiPolygon ...
            if geometries_types[0] in geometries_types[1] or geometries_types[1] in geometries_types[0]:
                return geometries_types[0]
        else:
            return geometry_collection.geom_type
        #geometries_types.append(feature.geom.geom_type)

    def define_geometry_type(self, geometry):
        if geometry.geom_type.lower() == 'geometrycollection':
            return self.define_geometry_collection_type(geometry).lower()
        return geometry.geom_type.lower()

    # todo: need refactoring
    def generate_geometric_image(self, geometry):
        spatial_references = {
            3857: "+init=epsg:3857",
            # font: https://help.openstreetmap.org/questions/13250/what-is-the-correct-projection-i-should-use-with-mapnik
            4326: "+init=epsg:4326",
            4674: "+proj=longlat +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +no_defs ",
            4618: "+proj=longlat +ellps=aust_SA +towgs84=-67.35,3.88,-38.22,0,0,0,0 +no_defs",
            9999: "+proj=lcc +ellps=GRS80 +lat_0=49 +lon_0=-95 +lat+1=49 +lat_2=77 +datum=NAD83 +units=m +no_defs"
        }
        map = mapnik.Map(800, 600)
        ds = mapnik.CSV(inline='wkt\n"' + geometry.wkt + '"', filesize_max=500)
        layer = mapnik.Layer('world')
        map.background = mapnik.Color('white')  # steelblue white

        geom_type = self.define_geometry_type(geometry)
        if geom_type not in ['polygon', 'multipolygon']:
            mapnik.load_map(map, 'style.xml')

            layer.srs = spatial_references[geometry.srs.srid]  # object.wkt.srs
            layer.datasource = ds
            layer.styles.append(geom_type)

            map.layers.append(layer)
            map.zoom_all()
            image = mapnik.Image(800, 600)
            mapnik.render(map, image)
            image.save('geometry.png')
            with open('geometry.png', 'rb') as geometry_png:
                data = geometry_png.read()
            os.remove('geometry.png')
            return data

        style = mapnik.Style()
        rule = mapnik.Rule()

        polygon_symbolizer = mapnik.PolygonSymbolizer()
        polygon_symbolizer.fill = mapnik.Color('#33AA33')#('#f2eff9')
        rule.symbols.append(polygon_symbolizer)

        line_symbolizer = mapnik.LineSymbolizer()
        line_symbolizer.stroke = mapnik.Color('rgb(90%,90%,90%)')
        line_symbolizer.stroke_width = 0.1
        rule.symbols.append(line_symbolizer)

        #point_symbolizer = mapnik.PointSymbolizer()#"marker-icon.png")
        #point_symbolizer.file = "marker-icon.png"
        #point_symbolizer.allow_overlap = True
        #rule.symbols.append(point_symbolizer)

        style.rules.append(rule)
        map.append_style('style', style)


        layer.srs = spatial_references[geometry.srs.srid]  # object.wkt.srs
        layer.datasource = ds
        layer.styles.append('style')
        map.layers.append(layer)
        map.zoom_all()
        mapnik.render_to_file(map, 'geometry.png', 'png')

        with open('geometry.png', 'rb') as geometry_png:
            data = geometry_png.read()
        os.remove('geometry.png')
        return data

#        if geometry.geom_type.lower() == 'geometrycollection':
#            geom_type = self.define_geometry_collection_type(geometry).lower()
#        else:
#            geom_type = geometry.geom_type.lower()
#        layer.styles.append(geom_type)

        #map.layers.append(layer)
        #map.zoom_all()
        #image = mapnik.Image(800, 600)
        #mapnik.render(map, image)
        #image.save('geometry.png')

