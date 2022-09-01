from django.contrib import admin
from .models import Product, OrderItem, Cart
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(Cart)
