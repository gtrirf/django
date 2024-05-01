from django.db import models

# Create your models here.


class Sayaboutyou(models.Model):
    sayaboutyou = models.CharField(max_length=555, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'about'

    def __str__(self):
        return self.name


class Bio(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    bio = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'bio'

    def __str__(self):
        return self.name