from django.db import models
from datetime import datetime
from chef.models import Chef


class Dish(models.Model):
    chef = models.ForeignKey(Chef, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    dish_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
