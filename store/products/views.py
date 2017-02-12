from django.shortcuts import render
from rest_framework import generics
from products.models import Products, Category, SubCategory
from products.serializers import ProductSerializer, CategorySerializer, SubCategorySerializer
from store.common import StandardResultsSetPagination

class ProductList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = StandardResultsSetPagination

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubCategoryList(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    pagination_class = StandardResultsSetPagination

class SubCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class ProductSubCategoryDetail(generics.ListAPIView):
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        product_id = self.kwargs['pk']
        product = Products.objects.get(pk=product_id)
        return SubCategory.objects.filter(id=product.productSubCategory_id)

class ProductCategoryDetail(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        product_id = self.kwargs['pk']
        product = Products.objects.get(pk=product_id)
        sub_cat = SubCategory.objects.get(id=product.productSubCategory_id)
        return Category.objects.filter(id=sub_cat.category.id)

