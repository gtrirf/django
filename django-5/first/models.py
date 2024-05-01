from django.db import models

# Create your models here.


class Product(models.Model):
    productname = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.productname


class Magazin(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    managername = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'magazin'

    def __str__(self):
        return self.name

