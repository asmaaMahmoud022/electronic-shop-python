from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    message = models.CharField(max_length=255)
