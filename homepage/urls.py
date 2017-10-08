from django.conf.urls import url

from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [url(r'^$', views.home, name="home"),
               url(r'^learnmore/$', views.learnmore, name="learnmore"),
               url(r'^about-us/$', views.aboutus, name="aboutus"),
               url(r'^pythonabout/$', views.pythonabout, name="pythonabout"),
               url(r'^.*/$', views.fourzerofour, name="fourzerofour"),
               ]

urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

