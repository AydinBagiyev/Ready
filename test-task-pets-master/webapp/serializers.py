from rest_framework import serializers

from webapp.models import Cat, Dog


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ('id', 'name', 'birthday')
        read_only = ('id', )


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ('id', 'name', 'birthday')
        read_only = ('id', )
