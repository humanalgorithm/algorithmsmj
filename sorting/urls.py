from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
                    url(r'^choosesort/$', 'sorting.views.choosesort'),
                    url(r'^quicksort/$', 'sorting.views.quicksort'),
                    url(r'^bubblesort/$', 'sorting.views.bubblesort'),
                    url(r'^mergesort/$', 'sorting.views.mergesort'),
                    url(r'^insertionsort/$', 'sorting.views.insertionsort'),
                    url(r'^selectionsort/$', 'sorting.views.selectionsort'),
                    url(r'^getdata/$', 'sorting.views.getdata'),
                      )

urlpatterns = format_suffix_patterns(urlpatterns)


