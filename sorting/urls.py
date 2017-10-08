from django.conf.urls import url
from views import quicksort, bubblesort, mergesort, insertionsort, selectionsort, get_random_dataset

urlpatterns = [
               url(r'^quicksort/$', quicksort, name="quicksort"),
               url(r'^bubblesort/$', bubblesort, name="bubblesort"),
               url(r'^mergesort/$', mergesort, name="mergesort"),
               url(r'^insertionsort/$', insertionsort, name="insertionsort"),
               url(r'^selectionsort/$', selectionsort, name="selectionsort"),
               url(r'^get_random_dataset/$', get_random_dataset, name="get_random_dataset"),
               ]