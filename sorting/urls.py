from django.conf.urls import url
from views import SortView
from views import AboutView
from views import DatasetView

urlpatterns = [
    url(r'^get_sort_result/$', SortView.as_view()),
    url(r'^get_random_dataset/$', DatasetView.as_view()),
    url(r'^about/(?P<sortname>[-\w]+)/$', AboutView.as_view()),
]
