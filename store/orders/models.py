from django.db import models

class Orders(models.Model):
    orderId = models.CharField(max_length=20, primary_key=True)
    orderDate = models.DateTimeField()
    customer = models.ForeignKey('customers.Customers', related_name="orders")
    products = models.ManyToManyField('products.Products', through='sales.Sales', related_name="orders")
