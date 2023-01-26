from rest_framework import serializers
from . import models


class ProductSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=14, decimal_places=2)
    description = serializers.CharField()
    amount = serializers.IntegerField()
    is_active = serializers.BooleanField(default=True)


class CategoriesSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=100)



