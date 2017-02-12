from django.db import models

class Shipments(models.Model):

    STANDARD_SHIPPING = "Standard Class"
    FIRST_CLASS = "First Class"
    SECOND_CLASS = "Second Class"
    SAME_DAY = "Same Day"
    
    SHIPPING_MODES = (
            (STANDARD_SHIPPING, "Standard Class"),
            (FIRST_CLASS, "First Class"),
            (SECOND_CLASS, "Second Class"),
            (SAME_DAY, "Same Day"),
            ) #This should be a class of its own with a table in the DB

    orderId = models.ForeignKey('orders.Orders')
    shipDate = models.DateTimeField()
    shipMode = models.CharField(max_length=50,choices=SHIPPING_MODES, default=STANDARD_SHIPPING)
