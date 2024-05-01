from django.db import models

# Create your models here.


class Administrators(models.Model):
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'admins'

    def __str__(self):
        return self.firstname


class Users(models.Model):
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.lastname

