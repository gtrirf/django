from django.db import models

# Create your models here.


class Users(models.Model):
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.lastname


class Contact(models.Model):
    number = models.IntegerField(default=998)
    telegram = models.CharField(max_length=255, blank=True, null=True)
    mail = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'contact'

    def __str__(self):
        return self.telegram

