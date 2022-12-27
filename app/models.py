from django.db import models

from django.db.models import JSONField


# Create your models here.

class CustomerData(models.Model):
    customer_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class OrderDetails(models.Model):
    customer_id = models.ForeignKey(CustomerData, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=100)
    order_date = models.DateField()
    order_status = models.CharField(max_length=100)
    order_items = JSONField()

    def __str__(self):
        return self.order_id
