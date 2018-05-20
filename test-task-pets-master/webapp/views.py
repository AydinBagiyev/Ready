from rest_framework import status, mixins, generics
from rest_framework.response import Response

from webapp.serializers import CatSerializer, DogSerializer


class BaseAnimalList(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BaseAnimalDetail(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class BaseCat(object):
    serializer_class = CatSerializer

    def get_queryset(self):
        return self.request.user.cats.all()


class BaseDog(object):
    serializer_class = DogSerializer

    def get_queryset(self):
        return self.request.user.dogs.all()


class CatList(BaseCat, BaseAnimalList):
    pass


class CatDetail(BaseCat, BaseAnimalDetail):
    pass


class DogList(BaseDog, BaseAnimalList):
    pass


class DogDetail(BaseDog, BaseAnimalDetail):
    pass