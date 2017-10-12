from django.conf.urls import url
from django.conf.urls import include

from django.contrib import admin

admin.autodiscover()
urlpatterns = [
               url(r'^admin/', admin.site.urls),
               url(r'', include('sorting.urls')),
               url(r'', include('signups.urls')),
               url(r'', include('homepage.urls')),
               ]
