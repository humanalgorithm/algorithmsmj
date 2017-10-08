

from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns = patterns('',
                    url(r'^api/$', views.SignUpList.as_view()),
                    url(r'^signups/', include('signups.urls')),
                       )

urlpatterns = format_suffix_patterns(urlpatterns)