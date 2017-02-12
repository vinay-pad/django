from django.conf.urls import include, url, patterns
from customers import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns([
    url(r'^$',
        views.CustomerList.as_view(),
        name='customers-list'),
    url(r'^(?P<pk>[A-Z]+-[0-9]+)/$',
        views.CustomerDetail.as_view(),
        name='customers-detail'),
    #url(r'^(?P<pk>[A-Z]+-[0-9]+)/segments/$',
    #    views.GetCustomerSegmentList.as_view(),
    #    name='customersegment-list'),
])
