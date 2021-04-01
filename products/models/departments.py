from django.db import models

class Department(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title 