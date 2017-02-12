from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from salaries import views

urlpatterns = [
    url(r'^$', views.SalaryList.as_view(), name='salary-list'),
    url(r'^(?P<pk>[a-z0-9]+)/$', views.SalaryDetail.as_view(), name='salary-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
