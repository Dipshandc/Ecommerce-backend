from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions  import IsAuthenticated
from ..models import *
from .serializers import *

class getRoutes(APIView):
    def get(self,request):
        routes = [
            '/api/token',
            '/api/token/refresh',
        ]
        return Response(routes)

class CustomerView(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self,request):
        customer = get_object_or_404(Customer,user=request.user)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, format=None):
     customer = get_object_or_404(Customer, user=request.user)
     serializer = CustomerSerializer(instance=customer, data=request.data, partial=True)
    
     if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_200_OK)
     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)