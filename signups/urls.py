from django.conf.urls import url
import views
from views import thankyou, signup

urlpatterns = [url(r'^api/$', views.SignUpList.as_view()),
               url(r'^thank-you/$', thankyou, name='thankyou'),
               url(r'^signup/$', signup, name='signup'),
               ]

