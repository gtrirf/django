from django.db import models

# Create your models here.


class Music(models.Model):
    author = models.CharField(max_length=255, blank=True, null=True)
    namemusic = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'musics'

    def __str__(self):
        return self.namemusic


class Movie(models.Model):
    rejjissor = models.CharField(max_length=255, blank=True, null=True)
    sennerist = models.CharField(max_length=255, blank=True, null=True)
    namemovie = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'kinolar'

    def __str__(self):
        return self.namemovie


