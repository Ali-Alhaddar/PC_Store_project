from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Pc(models.Model):
    name = models.CharField(max_length=100, default="")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=250)
    GPU = models.TextField(max_length=100, default="")
    CPU = models.TextField(max_length=100, default="")
    RAM = models.TextField(max_length=150, default="")
    storage = models.TextField(max_length=100, default="")
    motherboard = models.TextField(max_length=150, default="")
    image = models.ImageField(upload_to='main_app/static/uploads/', default="")

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pc_id': self.id})

class Monitor(models.Model):
    name = models.CharField(max_length=100, default="")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=250)
    screen_size = models.TextField(max_length=100, default="")
    resolution = models.TextField(max_length=100, default="")
    display_type = models.TextField(max_length=100, default="")
    image = models.ImageField(upload_to='main_app/static/uploads/', default="")

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'Monitor_id': self.id})

class Keybord(models.Model):
    name = models.CharField(max_length=100, default="")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to='main_app/static/uploads/', default="")

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'Keybord_id': self.id})
    
class CartItem(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.content_object}'