from django.conf.urls import include, url, patterns
from customers import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns([
    url(r'^$',
        views.SegmentList.as_view(),
        name='segment-list'),
    url(r'^(?P<pk>.+)/$',
        views.SegmentDetail.as_view(),
        name='segment-detail'),
])
