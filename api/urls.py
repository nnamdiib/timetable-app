from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import day_end_point, index, class_end_point

urlpatterns = {
    url(r'^index/$', index, name='index')
	, url(r'^dayend/$', day_end_point, name='dayendpoint')
	, url(r'^class/$', class_end_point, name='classendpoint')
}

urlpatterns = format_suffix_patterns(urlpatterns)