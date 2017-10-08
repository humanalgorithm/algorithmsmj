from django.conf.urls import url
from views import choosesort, quicksort, bubblesort, mergesort, insertionsort, selectionsort, getdata

urlpatterns = [
               url(r'^choosesort/$', choosesort, name="choosesort"),
               url(r'^quicksort/$', quicksort, name="quicksort"),
               url(r'^bubblesort/$', bubblesort, name="bubblesort"),
               url(r'^mergesort/$', mergesort, name="mergesort"),
               url(r'^insertionsort/$', insertionsort, name="insertionsort"),
               url(r'^selectionsort/$', selectionsort, name="selectionsort"),
               url(r'^getdata/$', getdata, name="getdata"),
               ]