from django.db import models

# Create your models here.


class Ismfamilya(models.Model):
    ism = models.CharField(max_length=64, blank=True, null=True)
    familya = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'ismlar'

    def __str__(self):
        return self.ism


class Maktab(models.Model):
    maktabraqami = models.IntegerField(default=1)
    status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'maktab'

    def __str__(self):
        return self.status

