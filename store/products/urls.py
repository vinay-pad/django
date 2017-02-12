from django.conf.urls import include, url, patterns
from products import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns([
    url(r'^$',
        views.ProductList.as_view(),
        name='products-list'),
    url(r'^(?P<pk>[0-9]+)/$',
        views.ProductDetail.as_view(),
        name='products-detail'),
    url(r'^(?P<pk>[0-9]+)/categories/$',
        views.ProductCategoryDetail.as_view(),
        name='productcategory-detail'),
    url(r'^(?P<pk>[0-9]+)/subcategories/$',
        views.ProductSubCategoryDetail.as_view(),
        name='productsubcategory-detail'),
])

#/v1/products/1/categories/
#/v1/products/1/subcategories/
