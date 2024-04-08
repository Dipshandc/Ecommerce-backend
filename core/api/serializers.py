from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ..models import *

class ProductSerializer(ModelSerializer):
  class Meta:
    model = Product
    fields = ['name','description','price']

class CartSerializer(ModelSerializer):
  class Meta:
    model = Cart
    fields = ['user','items']

class CartItemSerializer(ModelSerializer):
  class Meta:
    model = CartItem
    fields = ['cart','product','quantity']
    product = ProductSerializer
   