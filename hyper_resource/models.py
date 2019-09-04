from django.contrib.gis.db import models

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
        return self.geom.transfrom(coordinate_transformation, clone)