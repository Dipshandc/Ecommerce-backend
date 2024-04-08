from rest_framework.response import Response
from rest_framework.views import APIView
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
    



class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        carts = Cart.objects.filter(user=request.user)
        cart_serializer = CartSerializer(carts, many=True)
        cart_items_list = []
        for cart in carts:
            cart_items = CartItem.objects.filter(cart=cart)
            cart_items_serializer = CartItemSerializer(cart_items, many=True)
            cart_items_list.append(cart_items_serializer.data)

        response_data = {
            'cart': cart_serializer.data,
            'cart_items': cart_items_list
        }
        return Response(response_data)

    
class ProductView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
     query_set = Product.objects.all()
     serializer = ProductSerializer(query_set,many=True)
     return Response(serializer.data)