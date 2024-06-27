from django.shortcuts import render,redirect
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
from django.contrib.auth import logout
from django.urls import reverse
from .africas_talking import sms


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
 
    

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        order = serializer.save()
        customer = order.customer 
        phone_number = customer.phone_number 
        message = f"Dear {customer.name}, your order #{order.id} has been successfully placed."
        self.send_sms(phone_number, message)

    def send_sms(self, phone_number, message):
        try:
            if not str(phone_number).startswith('+'):
                phone_number = '+254' + str(phone_number) 

            response = sms.send(message, [phone_number])
            print(response)
        except Exception as e:
            print(f"Error while sending SMS: {e}")


    


def home (request):
    return render(request, 'api/home.html')