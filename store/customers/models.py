from django.db import models

class Address(models.Model):
    zipCode = models.CharField(max_length=5, primary_key=True) #needs validation
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    region = models.CharField(max_length=100)

class Customers(models.Model):
    customerId = models.CharField(max_length=50, primary_key=True)
    customerName = models.CharField(max_length=200)
    customerAddress = models.ForeignKey(Address, related_name="customers")

class Segment(models.Model):
    segment = models.CharField(max_length=100)

class CustomerSegment(models.Model):
    customer = models.ForeignKey(Customers, related_name="segments", to_field="customerId")
    segment = models.ForeignKey(Segment, related_name="customers")

    class Meta:
        unique_together = ('customer', 'segment',)
