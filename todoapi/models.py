from django.db import models
from django.conf import settings

class Todoapi(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='todoapi')
    title = models.CharField(max_length=100)
    completed = models.BooleanField()

    def __str__(self):
        return self.title