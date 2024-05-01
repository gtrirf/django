from django.db import models

# Create your models here.


class Items(models.Model):
    product = models.CharField(max_length=255, blank=True, null=True)
    make = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField(default=0)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'items'

    def __str__(self):
        return self.product


class Seller(models.Model):
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'sellers'

    def __str__(self):
        return self.lastname