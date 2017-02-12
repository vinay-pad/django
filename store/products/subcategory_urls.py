from django.conf.urls import include, url, patterns
from products import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns([
    url(r'^$',
        views.SubCategoryList.as_view(),
        name='subcategory-list'),
    url(r'^(?P<pk>[0-9]+)/$',
        views.SubCategoryDetail.as_view(),
        name='subcategory-detail'),
])
