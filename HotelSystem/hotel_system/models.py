from django.db import models

class Hotel (models.Model):

    date = models.DateField()
    day = models.TextField(max_length=20)
    price_single = models.IntegerField()
    avail_single = models.IntegerField()
    price_double = models.IntegerField()
    avail_double = models.IntegerField()
    month=models.TextField(max_length=20, null=True )
    year=models.IntegerField(null=True)
    month_year=models.TextField(max_length=20, null = True)