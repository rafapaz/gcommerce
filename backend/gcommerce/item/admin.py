from django.contrib import admin
from .models import Item, ItemCategory, ItemRating, ItemPhoto

admin.site.register(Item)
admin.site.register(ItemCategory)
admin.site.register(ItemRating)
admin.site.register(ItemPhoto)
