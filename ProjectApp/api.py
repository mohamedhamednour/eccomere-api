from rest_framework import serializers
from .models import Product, OrderItem, Cart
from django.contrib.auth.models import User


class Products(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        depth = 1



class order(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = '__all__'
        depth = 1



class cart(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'
        depth = 1



class USer_register(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password',
                  'email', 'first_name', 'last_name')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
