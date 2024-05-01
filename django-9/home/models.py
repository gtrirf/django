from django.db import models

# Create your models here.


class TrueorFalse(models.Model):
    atvet = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'atvet'

    def __str__(self):
        return self.atvet


class YesorNO(models.Model):
    otvet = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'otvet'

    def __str__(self):
        return self.otvet

