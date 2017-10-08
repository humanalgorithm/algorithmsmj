from sorting import urls

from django.conf import settings
from django.conf.urls import patterns, include

from homepage import urls
from signups import urls

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       (r'admin/', include(admin.site.urls)),
                       (r'', include('homepage.urls')),
                       (r'', include('signups.urls')),
                       (r'', include('sorting.urls'))
                       )
