from django.contrib.gis.db import models
from django.contrib.gis.geos import GeometryCollection
from django.db.models import Q


class CollectionModel(models.Model):
    @staticmethod
    def filter(object_class, q_object):
        return object_class.objects.filter(q_object)

class FeatureCollectionModel(CollectionModel):
    #class Meta:
    #    abstract = True


    # example: http://localhost:8000/api/restful-ide/bcim/trecho-rodoviario/crosses/http://localhost:8000/api/restful-ide/bcim/unidades-federativas/MG
    @staticmethod
    def crosses(object_class, geometry):
        return object_class.objects.filter(geom__crosses=geometry)

    # http://localhost:8000/api/restful-ide/bcim/capital/within/http://localhost:8000/api/restful-ide/bcim/unidades-federativas/SP/
    @staticmethod
    def within(object_class, geometry):
        return object_class.objects.filter(geom__within=geometry)

class FeatureModel(models.Model):
    class Meta:
        abstract = True

    def area(self):
        return self.geom.area

    def buffer(self, width, quadsegs=8):
        return self.geom.buffer(width, quadsegs=quadsegs)

    def envelope(self):
        return self.geom.envelope

    def transform(self, coordinate_transformation, clone=True):
        '''
        :param coordinate_transformation type: int:
        :param clone:
        :return:
        '''
        return self.geom.transform(coordinate_transformation, clone)