from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.charField(max_length=255)
    code = models.charField(max_length=100, unique=True)
    phone_number = models.charField(max_length=15)


class Order (models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    item = models.charField(max_length=255)
    amount = models.DecimalField(max_digit=10, decimal_places=2)
    time = models.DateTimeField()
