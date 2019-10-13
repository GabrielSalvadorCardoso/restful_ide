from rest_framework.response import Response

from hyper_resource.resources.AbstractResource import AbstractResource, RequiredObject, JSON_CONTENT_TYPE, OPERATION_KWARGS_LABEL
from hyper_resource.operations import InvalidOperationException

class AbstractCollectionResource(AbstractResource):

    def basic_get(self, request, *args, **kwargs):
        queryset = self.serializer_class.Meta.model.objects.all()
        serializer = self.serializer_class(queryset, many=True, context={'request': request})
        return RequiredObject(serializer.data, JSON_CONTENT_TYPE, 200)

    def get(self, request, *args, **kwargs):
        required_object = self.basic_get(request, *args, **kwargs)
        return Response(
            required_object.representation_object,
            status=required_object.status_code,
            content_type=required_object.content_type
        )