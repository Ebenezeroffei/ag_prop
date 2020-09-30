from django.db import models

# Create your models here.
class Property(models.Model):
    category_choices = [
        ('Sale','Sale'),
        ('Rent','Rent'),
        ('Buy','Buy')
    ]
    name = models.CharField(max_length = 100);
    price = models.DecimalField(decimal_places = 2,max_digits = 100000)
    location =  models.CharField(max_length = 100)
    category = models.CharField(max_length = 10,choices = category_choices)