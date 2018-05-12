from django.db import models

class Hotel (models.Model):

    date = models.DateField(auto_now=True)
    day = models.TextField(max_length=20)
    price_single = models.IntegerField()
    avail_single = models.IntegerField()
    price_double = models.IntegerField()
    avail_double = models.IntegerField()

