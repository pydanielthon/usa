from django.db import models

# Create your models here.


class Formularz(models.Model):
    document1 = models.FileField(upload_to='documents/%Y/%m/%d')
    document2 = models.FileField(upload_to='documents/%Y/%m/%d')
    document3 = models.FileField(upload_to='documents/%Y/%m/%d')

    link1 = models.CharField(max_length=9999)
    link2 = models.CharField(max_length=9999)
    link3 = models.CharField(max_length=9999)
