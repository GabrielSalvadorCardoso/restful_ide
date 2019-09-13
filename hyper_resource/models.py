from django.contrib.gis.db import models
from django.contrib.gis.geos import GeometryCollection

class FeatureCollectionModel(models.Model):
    #class Meta:
    #    abstract = True

    @staticmethod
    def within(object_class, geometry):
        return object_class.objects.filter(geom__within=geometry)

class FeatureModel(models.Model):
    class Meta:
        abstract = True

    def envelope(self):
        return self.geom.envelope

    def transform(self, coordinate_transformation, clone=True):
        '''
        :param coordinate_transformation type: int:
        :param clone:
        :return:
        '''
        return self.geom.transform(coordinate_transformation, clone)