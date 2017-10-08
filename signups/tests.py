
from django.shortcuts import HttpResponse

import json
import sort
import time

from multiprocessing import Process, Queue
import threading
import multiprocessing

def mergesort():
    timeout = .00000001
    input = [33,6,7,2,78,2,7,3,2,7,3,2,23,234,234,234,234,6,2,7,2,21,7,2,234,7,8,235,23,2,5,235]
    global timeout
    que = Queue()
    thr = threading.Thread(target = lambda q, arg : q.put(sort.startMergeSort(input)), args = (que, 2))

    thr.start()
    thr.join(timeout)
    if thr.is_alive():
        thr._Thread__stop()
        print "thread weas killed!"
        data = json.dumps({
       "array": input,
      "time": 0
          })
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        returnarr = que.get()
        data = json.dumps({
        "array": returnarr,
        "time": 6
          })
        print "data to return is " +json.dumps(data)
        return HttpResponse(json.dumps(data), content_type='application/json')


def test():


    input = [33,6,7,2,78,2,7,3,2,7,3,2,23,234,234,234,234,6,2,7,2,21,7,2,234,7,8,235,23,2,5,235]
   # decoded = json.loads(input)

    time_begin = time.clock()
    print "time begin" + str(time_begin)

    p = multiprocessing.Process(target=sort.mergeSort(input,))
    #decoded = sort.startMergeSort(decoded)
    p.start()
    p.join(.000001)
    if p.is_alive():
        p.terminate()
        print "thread weas killed!"

    print ""
    time_end = time.clock()
    print "time end: " + str(time_end)
    time_elapsed = time_end - time_begin
    print "time elapsed" + str(time_elapsed)

    # pretty printing of json-formatted string
    print json.dumps(input, sort_keys=True, indent=4)

    data = json.dumps({
        "array":  input,
        "time": time_elapsed
    })
    return HttpResponse(json.dumps(data), content_type='application/json')


mergesort()