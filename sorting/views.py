import json
from service.service import SortService
from django.shortcuts import render
from dataset.dataset_builder import DatasetBuilder
from timed_thread.thread_runner import ThreadRunner

from django.http import HttpResponse
from django.views.generic.base import View


class AboutView(View):
    def get(self, request, sortname):
        template_map = {
            "bubblesort": "sort_about/bubblesortabout.html",
            "selectionsort": "sort_about/selectionsortabout.html",
            "insertionsort": "sort_about/insertionsortabout.html",
            "mergesort": "sort_about/mergesortabout.html",
            "quicksort": "sort_about/quicksortabout.html"
        }
        template = template_map.get(sortname)
        if not template:
            return render(request, "page/404.html")
        return render(request, template)

class SortView(View):
    def post(self, request):
        dataset = self._parse_dataset(request.POST)
        sort_name = request.POST.get('sort_name')
        if not dataset or not sort_name:
            return_json = {"error": "Invalid dataset was submitted"}
            return HttpResponse(json.dumps(return_json), content_type="application/json", status=400)

        return_json = self._get_sort_result(dataset, sort_name)
        return HttpResponse(json.dumps(return_json), content_type="application/json", status=200)

    def _parse_dataset(self, post):
        try:
            submitted_dataset = [int(i) for i in post.getlist("dataset")]
            return submitted_dataset
        except:
            return None

    def _get_sort_result(self, dataset, sort_name):
        sort_func = SortService(sort_method=sort_name).get_sort_func()
        thread_result = ThreadRunner(func=sort_func, data=dataset).run_in_thread()
        return {"sorted_dataset": thread_result.get_thread_result(), "time": thread_result.get_time_alotted()}

class DatasetView(View):
    def post(self, request):
        status_code = 200
        return_msg = self._get_random_dataset(request)
        if return_msg == -1:
            return_msg = {"error": "Requested array size is too big"}
            status_code = 400
        return HttpResponse(json.dumps(return_msg), content_type='application/json', status=status_code)

    def _get_random_dataset(self, request):
        arraysize = request.POST.get("dataset_size")
        return_msg = DatasetBuilder().get_random_dataset(arraysize)
        return return_msg
