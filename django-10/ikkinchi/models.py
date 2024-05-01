from django.db import models

# Create your models here.


class Djangopro(models.Model):
    projectname = models.CharField(max_length=255, blank=True, null=True)
    nechanchiproject = models.IntegerField(default=10)

    class Meta:
        db_table = 'finally'

    def __str__(self):
        return self.projectname


class Finallypro(models.Model):
    oxirgisimi = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'project'

    def __str__(self):
        return self.oxirgisimi