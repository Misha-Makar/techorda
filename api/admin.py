from django.contrib import admin
from . import models


# class CategoriesInline(admin.TabularInline):
#     model = models.Categories
#     extra = 1
#
#
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('Is active', 'Details')
#     inlines = (CategoriesInline,)


admin.site.register(models.Categories)
admin.site.register(models.Product)