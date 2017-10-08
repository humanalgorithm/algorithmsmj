from django.conf.urls import patterns,include, url
from django.contrib.auth.models import User


from django.contrib import admin
admin.autodiscover()

from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',

         url(r'^$', 'homepage.views.home', name="home"),
         url(r'^learnmore/$', 'homepage.views.learnmore', name="learnmore"),
         url(r'^about-us/$', 'homepage.views.aboutus', name="aboutus"),
         url(r'^pythonabout/$', 'homepage.views.pythonabout'),
         url(r'^.*/$', 'homepage.views.fourzerofour')
)

urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)

