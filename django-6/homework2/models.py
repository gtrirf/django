from django.db import models

# Create your models here.


class Student(models.Model):
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    grade = models.IntegerField(default=1)

    class Meta:
        db_table = "students"

    def __str__(self):
        return self.firstname


class Teacher(models.Model):
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    classes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'teachers'

    def __str__(self):
        return self.lastname

