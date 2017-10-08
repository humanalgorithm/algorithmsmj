from django.conf.urls import patterns,include, url
from django.contrib.auth.models import User


from django.contrib import admin
admin.autodiscover()

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',

         url(r'^$', 'homepage.views.home', name='home'),
         url(r'^thank-you/$', 'homepage.views.thankyou', name='thankyou'),
        url(r'^learnmore/$', 'homepage.views.learnmore', name='learnmore'),
         url(r'^about-us/$', 'signups.views.aboutus', name='aboutus'),
         url(r'^admin/', include(admin.site.urls)),
         url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

         url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
         url(r'^selectionsortabout/$', 'signups.views.selectionsortabout', name='selectionsortabout'),
         url(r'^pythonabout/$', 'signups.views.pythonabout', name='pythonabout'),
         url(r'^.*/$', 'signups.views.fourzerofour', name='fourzerofour')
)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


