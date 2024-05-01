from django.db import models

# Create your models here.


class Firstname(models.Model):
    firstname = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'firstname'

    def __str__(self):
        return self.firstname


class Lastname(models.Model):
    lastname = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'lastname'

    def __str__(self):
        return self.lastname
