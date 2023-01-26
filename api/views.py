from django.shortcuts import get_list_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from api import serializers, models


class ProductViewSet(ViewSet):

    def list(self, request, *args, **kwargs):
        model = models.Product.objects.all()
        serializer = serializers.ProductSerializer(model, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        model = get_list_or_404(models.Product.objects.all(), pk=pk)
        serializer = serializers.ProductSerializer(model, many=True)
        return Response(serializer.data)


class CategoriesViewSet(ViewSet):

    def list(self, request, *args, **kwargs):
        model = models.Categories.objects.all()
        serializer = serializers.CategoriesSerializer(model, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        model = get_list_or_404(models.Product.objects.all(), pk=pk)
        serializer = serializers.CategoriesSerializer(model)
        return Response(serializer.data)
