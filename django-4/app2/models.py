from django.db import models

# Create your models here.


class Edu(models.Model):
    kurs = models.CharField(max_length=255, blank=True, null=True)
    oyliktulov =models.IntegerField(default=50000)

    class Meta:
        db_table = 'edu'

    def __str__(self):
        return self.kurs


class Teacher(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    kurs = models.CharField(max_length=255, blank=True, null=True)
    sallery = models.IntegerField(default=0)

    class Meta:
        db_table = 'teachers'

    def __str__(self):
        return self.name

