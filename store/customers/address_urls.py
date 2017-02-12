from django.conf.urls import include, url, patterns
from customers import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns([
    url(r'^$',
        views.AddressList.as_view(),
        name='address-list'),
    url(r'^(?P<pk>.+)/$',
        views.AddressDetail.as_view(),
        name='address-detail'),
])

