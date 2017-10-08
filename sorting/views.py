import json
import sort
import time
from django.views.decorators.csrf import ensure_csrf_cookie
from multiprocessing import Queue, Process
import threading
import multiprocessing
from django.shortcuts import render_to_response, RequestContext, HttpResponseRedirect
from django.shortcuts import HttpResponse


def getsort(request, sortname):
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

def getdata(request):
    returnarray = sort.randomize()
    return HttpResponse(json.dumps(returnarray), content_type='application/json')

def choosesort(request):
    global maxarray
    arraysize = request.POST["arraysize"]
    if int(arraysize) > int(maxarray):
        return HttpResponse(status=500, content_type='application/json')
    try:
        returnarray = sort.randomize(arraysize)
    except:
        return HttpResponse(status=500, content_type='application/json')
    return HttpResponse(json.dumps(returnarray), content_type='application/json')


def quicksortabout(request):
    return render_to_response("quicksortabout.html",
                              locals(),
                              context_instance =RequestContext(request))
def mergesortabout(request):
    return render_to_response("mergesortabout.html",
                              locals(),
                              context_instance =RequestContext(request))

def bubblesortabout(request):
    return render_to_response("bubblesortabout.html",
                              locals(),
                              context_instance =RequestContext(request))
def insertionsortabout(request):
    return render_to_response("insertionsortabout.html",
                              locals(),
                              context_instance =RequestContext(request))
def selectionsortabout(request):
    return render_to_response("selectionsortabout.html",
                              locals(),
                              context_instance =RequestContext(request))
