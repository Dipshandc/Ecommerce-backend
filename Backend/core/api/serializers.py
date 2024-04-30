from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ..models import *


class CustomerSerializer(ModelSerializer):
  class Meta:
    model = Customer
    fields =['user','first_name','last_name','email','phone','birth_date']

class ProductSerializer(ModelSerializer):
  class  Meta:
    model = Product
    fields = ['title','description','price','inventory','last_update']

class CartSerializer(ModelSerializer):
  class Meta:
    model = Cart
    fields = ['id']
