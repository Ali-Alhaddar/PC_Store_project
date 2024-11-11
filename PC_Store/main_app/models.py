from django.db import models
from django.urls import reverse

class Pc(models.Model):
    name = models.CharField(max_length=100, default="")
    description = models.TextField(max_length=250)
    GPU = models.TextField(max_length=100, default="")
    CPU = models.TextField(max_length=100, default="")
    RAM = models.TextField(max_length=100, default="")
    storage = models.TextField(max_length=100, default="")
    motherboard = models.TextField(max_length=150, default="")
    image = models.ImageField(upload_to='main_app/static/uploads/', default="")

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pc_id': self.id})