from django.urls import path
from .import views
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    
)

urlpatterns = [
    path('',views.getRoutes.as_view()),
    path('token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
    path('cart/',CartView.as_view(), name='cart'),
    path('products/',ProductView.as_view(), name='products'),

]