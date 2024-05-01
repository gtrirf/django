from django.db import models

# Create your models here.


class Name(models.Model):
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'names'

    def __str__(self):
        return self.firstname


class Office(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    workers = models.IntegerField(default=0)
    money = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'office'

    def __str__(self):
        return self.name

