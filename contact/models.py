from django.db import models
from datetime import datetime


class Contact(models.Model):
    dish = models.CharField(max_length=255)
    dish_id = models.IntegerField()
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name
