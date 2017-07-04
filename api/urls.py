from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ClassListCreate, ClassList, DayList, DayListCreate, day_end_point, index

urlpatterns = {
    url(r'^index/$', index, name='index')
	, url(r'^classes/$', ClassListCreate.as_view(), name='classlistcreate')
	, url(r'^classes/(?P<codes>.+)/$', ClassList.as_view(), name='classlist')
	, url(r'^days/(?P<codes>.+)/$', DayList.as_view(), name='daylist')
	, url(r'^days/$', DayListCreate.as_view(), name='daylistcreate')
	, url(r'^dayend/$', day_end_point, name='dayendpoint')
}

urlpatterns = format_suffix_patterns(urlpatterns)