from django.db import models

# Create your models here.


class Ideaqomadiuje(models.Model):
    ideabormi = models.CharField(max_length=255,  default='yoq')

    class Meta:
        db_table = 'idea'

    def __str__(self):
        return self.ideabormi


class Hayoq(models.Model):
    hamiyoqmi = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'hayokiyoq'

    def __str__(self):
        return self.hamiyoqmi