from django.db import models

# Create your models here.


class Names(models.Model):
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'names'

    def __str__(self):
        return self.firstname


class Jobs(models.Model):
    where = models.CharField(max_length=255, blank=True, null=True)
    jobname = models.CharField(max_length=255, blank=True, null=True)
    sallary = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'jobs'

    def __str__(self):
        return self.jobname
