import json
import time
from django.views.decorators.csrf import ensure_csrf_cookie
from multiprocessing import Queue, Process
import threading
from django.shortcuts import HttpResponse, render
from dataset.dataset_builder import DatasetBuilder


def getsort(request, sortname):
    pass
    '''
    input = request.POST["array"]
    decoded = json.loads(input)
    if decoded[0] == None:
        return HttpResponse(status=500, content_type='application/json')

    global timeout
    que = Queue()

    if sortname == "mergesort":
        thr = threading.Thread(target = lambda q, arg : q.put(sort.startMergeSort(decoded, timeout)), args = (que, 2))
    elif sortname == "quicksort":
        thr = threading.Thread(target = lambda q, arg : q.put(sort.quickSortStart(decoded,timeout)), args = (que, 2))
    elif sortname =="insertionsort":
        thr = threading.Thread(target = lambda q, arg : q.put(sort.startInsertionSort(decoded, timeout)), args = (que, 2))
    elif sortname == "bubblesort":
         thr = threading.Thread(target = lambda q, arg : q.put(sort.startBubbleSort(decoded, timeout)), args = (que, 2))
    elif sortname == "selectionsort":
         thr = threading.Thread(target = lambda q, arg : q.put(sort.startSelectionSort(decoded, timeout)), args = (que, 2))

    thr.daemon = True
    time_start = time.clock()
    try:
        thr.start()
        thr.join(timeout)
    except:
        return HttpResponse(status=500, content_type='application/json')
    if thr.is_alive():
        thr._Thread__stop()
        print "thread weas killed!"
        data = json.dumps({
        "array": decoded,
        "time": timeout,
        "error": "timeout"
          })
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        time_end = time.clock()
        elapsed_time = time_end-time_start
        returnarr = que.get()
        data = json.dumps({
        "array": returnarr,
        "time": elapsed_time
          })
        return HttpResponse(json.dumps(data), content_type='application/json')
    '''

def mergesort(request):
    sortname = "mergesort"
    return getsort(request,sortname)

def bubblesort(request):
    sortname = "bubblesort"
    return getsort(request,sortname)

def quicksort(request):
    sortname = "quicksort"
    return getsort(request,sortname)

def selectionsort(request):
    sortname = "selectionsort"
    return getsort(request,sortname)

def insertionsort(request):
    sortname = "insertionsort"
    return getsort(request,sortname)

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
