from django.db import models

class Sales(models.Model):
    order = models.ForeignKey('orders.Orders')
    product = models.ForeignKey('products.Products')
    salesIncome = models.DecimalField(max_digits=19, decimal_places=4)
    quantity = models.SmallIntegerField()
    discount = models.DecimalField(max_digits=19, decimal_places=4)
    profit = models.DecimalField(max_digits=19, decimal_places=4)

