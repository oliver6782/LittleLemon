from django.shortcuts import render
from rest_framework import response, generics
from .models import Category, Cart, MenuItem, Order,OrderItem
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User, Group
from .serializers import CategorySerializer, MenuItemSerializer
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .paginations import MenuItemPagination



class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    
class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAdminUser]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    pagination_class = MenuItemPagination
    ordering_fields = ['price']
    search_fields = ['title', 'category']