from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import day_end_point, class_end_point, index, clear_table

urlpatterns = {
	url(r'^$', index, name='index')
    , url(r'^index/$', index, name='index')
	, url(r'^classes/$', class_end_point, name="classendpoint")
	, url(r'^dayend/$', day_end_point, name='dayendpoint')
	, url(r'^clear-table/$', clear_table, name='clear_table')
}

urlpatterns = format_suffix_patterns(urlpatterns)