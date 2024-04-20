from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ..models import *


class CustomerSerializer(ModelSerializer):
  class Meta:
    model = Customer
    fields =['user','first_name','last_name','email','phone','birth_date']

