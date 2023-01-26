from django.db import models
from django.utils.translation import gettext_lazy as _


class Categories(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('NAME'), unique=True)
    price = models.DecimalField(max_digits=14, decimal_places=2, verbose_name=_('PRICE'))
    description = models.TextField(verbose_name=_('Details'))
    amount = models.IntegerField()
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))






