from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=False)
    price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    order_user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} - {self.cart}"


class Cart(models.Model):
    order_user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)
    total = models.IntegerField(default=0)

    def __int__(self):
        return self.product

    def __str__(self):
        return f"{self.id} - {self.product}"

    def get_total(self):
        return round(float(self.product.price) * float(self.quantity))

    def save(self, *args, **kwargs):
        self.total = self.get_total()
        super().save(*args, **kwargs)
