from django.db import models

# Create your models here.


class Pubg(models.Model):
    iduser = models.IntegerField(default=512)
    nick = models.CharField(max_length=255, blank=True, null=True)
    level = models.IntegerField(default=1)

    class Meta:
        db_table = 'pubg'

    def __str__(self):
        return self.nick


class Insta(models.Model):
    nick = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    bio = models.CharField(max_length=555, blank=True, null=True)

    class Meta:
        db_table = 'insta'

    def __str__(self):
        return self.nick

