from django.contrib import admin
from django.urls import path
from api import views


urlpatterns = [

    path('product/', views.ProductViewSet.as_view({'get': 'list'})),
    path('product/<int:pk>', views.ProductViewSet.as_view({'get': 'retrieve'})),
    path('categories/', views.CategoriesViewSet.as_view({'get': 'list'})),
    path('categories/<int:pk>', views.CategoriesViewSet.as_view({'get': 'retrieve'})),
]

