from monitor import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url

app_name = 'monitor'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/$', views.MonitorList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
