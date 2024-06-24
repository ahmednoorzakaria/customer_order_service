from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
# Create your views here.


class CustomerViewSet(viewsets.ModelViewsSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OrderViewSet (viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
