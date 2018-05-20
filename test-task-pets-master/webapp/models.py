from django.db import models
from django.conf import settings


class Animal(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField()

    class Meta:
        abstract = True


class Dog(Animal):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='dogs')

    def __str__(self):
        return self.name


class Cat(Animal):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='cats')

    def __str__(self):
        return self.name
