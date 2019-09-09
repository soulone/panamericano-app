from django.db import models

class Deporte(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
