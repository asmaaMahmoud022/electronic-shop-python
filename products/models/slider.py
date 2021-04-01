from django.db import models

class Slider(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField()
    active = models.BooleanField(default=False)
