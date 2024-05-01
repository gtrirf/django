from django.db import models

# Create your models here.


class Cars(models.Model):
    make = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    year = models.DateField(blank=True, null=True)
    price = models.IntegerField(default=0)
    color = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'cars'

    def __str__(self):
        return self.model


class Avtosalon(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    boss = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'avtosalon'

    def __str__(self):
        return self.name


