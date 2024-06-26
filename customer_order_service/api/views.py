from django.shortcuts import render,redirect
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
from django.contrib.auth import logout
from django.urls import reverse


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    def initial(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse('account_login'))
        return super().initial(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        logout(request)
        return redirect('/accounts/login/')


class OrderViewSet (viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def initial(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse('account_login'))
        return super().initial(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        logout(request)
        return redirect('/accounts/login/')



def home (request):
    return render(request, 'api/home.html')