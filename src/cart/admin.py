from django.contrib import admin
from .models import ColourVariation, Product, Order, OrderItem,SizeVariation
# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ColourVariation)
admin.site.register(SizeVariation)