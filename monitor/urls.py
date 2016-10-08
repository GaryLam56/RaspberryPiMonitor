from monitor import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url

app_name = 'monitor'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^api/$', views.MonitorList.as_view()),
    url(r'^login/$', views.login_user, name='login_user'),
    url(r'^test/$', views.test, name='test'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
