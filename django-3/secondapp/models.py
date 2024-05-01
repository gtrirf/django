from django.db import models

# Create your models here.


class School(models.Model):
    schoolnumber = models.IntegerField(default=1)
    status = models.CharField(max_length=255, blank=True, null=True)
    student = models.IntegerField(default=0)

    class Meta:
        db_table = 'school'

    def __str__(self):
        return self.status


class University(models.Model):
    nameuni = models.CharField(max_length=255, blank=True, null=True)
    courses = models.CharField(max_length=255, blank=True, null=True)
    student = models.IntegerField(default=0)

    class Meta:
        db_table = 'university'

    def __str__(self):
        return self.nameuni

