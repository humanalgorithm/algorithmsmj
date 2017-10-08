from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns = patterns('',
                    url(r'^api/$', views.SignUpList.as_view()),
                    url(r'^thank-you/$', 'signups.views.thankyou', name='thankyou'),
                    url(r'^signup/$', 'signups.views.signup', name='signup'),
                       )

urlpatterns = format_suffix_patterns(urlpatterns)