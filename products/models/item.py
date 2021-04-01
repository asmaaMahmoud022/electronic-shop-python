from django.db import models
from . import departments

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to='products/media/items')
    department = models.ManyToManyField(departments.Department, related_name = 'departments')
    visible = models.BooleanField(default=False)
