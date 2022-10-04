from django.db import models
from datetime import datetime


class Chef(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    hire_date = models.DateTimeField(datetime.now, blank=True)

    def __str__(self):
        return self.name
