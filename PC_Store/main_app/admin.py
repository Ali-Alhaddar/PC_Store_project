from django.contrib import admin
from .models import Pc, CartItem, Monitor, Keybord

# Register your models here.

admin.site.register(Pc)
admin.site.register(Monitor)
admin.site.register(Keybord)
admin.site.register(CartItem)