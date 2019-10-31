from django.contrib import admin
from .models import Order, ItemOrder, Cart

admin.site.register(Order)
admin.site.register(ItemOrder)
admin.site.register(Cart)
