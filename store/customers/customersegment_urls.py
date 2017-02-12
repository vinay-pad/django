from django.conf.urls import include, url, patterns
from customers import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns([
    url(r'^$',
        views.CustomerSegmentList.as_view(),
        name='customersegment-list'),
    url(r'^(?P<pk>.+)/$',
        views.CustomerSegmentDetail.as_view(),
        name='customersegment-detail'),
])
