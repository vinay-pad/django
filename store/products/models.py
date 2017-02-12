from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=50)

class SubCategory(models.Model):
    category = models.ForeignKey(Category, related_name="sub_categories")
    subCategory = models.CharField(max_length=50)

class Products(models.Model):
    productId = models.CharField(max_length=20)
    productName = models.CharField(max_length=100)
    productSubCategory = models.ForeignKey(SubCategory, related_name="products")
    productCategory = models.ForeignKey(Category, related_name="products")
