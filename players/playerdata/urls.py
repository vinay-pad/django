from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from playerdata import views

urlpatterns = [
    url(r'^$', views.PlayerList.as_view(), name='player-list'),
    url(r'^(?P<pk>[a-z0-9]+)/$', views.PlayerDetail.as_view(), name='player-detail'),
    url(r'^(?P<playerid>[a-z0-9]+)/salaries/$', views.PlayerSalaryDetail.as_view(), name='player-salary-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
