from django.db import models


# Create your models here.
class Pc(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to='main_app/static/uploads/', default="")
