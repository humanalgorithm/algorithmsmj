import json
from service.service import SortService
from django.shortcuts import HttpResponse, render
from dataset.dataset_builder import DatasetBuilder
from timed_thread.thread_runner import ThreadRunner

from django.http import HttpResponse
from django.views.generic.base import View


class SortView(View):
    def post(self, request):
        dataset = self._parse_dataset(request.POST)
        sort_name = request.POST.get('sort_name')

        if not dataset or not sort_name:
            status_code = 400
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

def get_random_dataset(request):
    arraysize = request.POST.get("dataset_size")
    return_msg = DatasetBuilder().get_random_dataset(arraysize)
    status_code = 200
    if return_msg == -1:
        return_msg = {"error": "Requested array size is too big"}
        status_code = 400
    return HttpResponse(json.dumps(return_msg), content_type='application/json', status=status_code)

def quicksortabout(request):
    return render(request, "quicksortabout.html")

def mergesortabout(request):
    return render(request, "mergesortabout.html")

def bubblesortabout(request):
    return render(request, "bubblesortabout.html")

def insertionsortabout(request):
    return render(request, "insertionsortabout.html")

def selectionsortabout(request):
    return render(request, "selectionsortabout.html")
