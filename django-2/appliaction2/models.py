from django.db import models

# Create your models here.


class Books(models.Model):
    author = models.CharField(max_length=255, blank=True, null=True)
    namebook = models.CharField(max_length=255, blank=True, null=True)
    price = models.IntegerField(default=0)

    class Meta:
        db_table = 'books'

    def __str__(self):
        return self.namebook


class Bookshop(models.Model):
    shopname = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'bookshop'

    def __str__(self):
        return self.shopname

