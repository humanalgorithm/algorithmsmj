from django.conf.urls import url
from views import get_random_dataset
from views import SortView

urlpatterns = [
               url(r'^get_sort_result/$', SortView.as_view()),
               url(r'^get_random_dataset/$', get_random_dataset, name="get_random_dataset"),
               ]