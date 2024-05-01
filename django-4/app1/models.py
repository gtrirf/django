from django.db import models

# Create your models here.


class Computer(models.Model):
    processor = models.CharField(max_length=255, blank=True, null=True)
    make = models.CharField(max_length=255, blank=True, null=True)
    gpu = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'computer'

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    founder = models.CharField(max_length=255, blank=True, null=True)
    est = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'company'

    def __str__(self):
        return self.name

