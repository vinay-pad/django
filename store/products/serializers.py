from rest_framework import serializers
from products.models import Products, Category, SubCategory

class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.HyperlinkedRelatedField(view_name='category-detail', read_only=True)
    #category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    class Meta:
        model = SubCategory
        fields = ('url', 'category', 'subCategory',)

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    sub_categories = serializers.HyperlinkedRelatedField(many=True, view_name='subcategory-detail', read_only=True)
    #sub_categories = serializers.PrimaryKeyRelatedField(queryset=SubCategory.objects.all(), many=True)
    class Meta:
        model = Category
        fields = ('url', 'category', 'sub_categories',)

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    #productSubCategory = serializers.PrimaryKeyRelatedField(queryset=ProductSubCategory.objects.all())
    productSubCategory = serializers.HyperlinkedRelatedField(view_name='subcategory-detail', queryset=SubCategory.objects.all())
    productCategory = serializers.HyperlinkedRelatedField(view_name='category-detail', queryset=Category.objects.all())

    class Meta:
        model = Products
        fields = ('url', 'productId', 'productName', 'productCategory', 'productSubCategory', )
