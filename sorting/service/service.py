from .factory import SortFactory

class SortService(object):
    def __init__(self, array, sort_method):
        sort_obj = SortFactory(sort_method)
        return self.sort(array, sort_obj)

    def sort(self, array, sort_obj):
        return sort_obj().run_sort(array)

'''
import random
import time
from multiprocessing import Process, Queue
import threading
import multiprocessing


#intialize global variables
mylist=[]
lastarray=[]
timerStart= 0
timeElapsed = 0
sortName = "Please select sort"
lastRandom = False

bubbleSortName = "Bubble sort with an expected run time of O(N^2)"
quickSortName = "Quick sort with an expected run time of O(n log n)"
mergeSortName = "Merge Sort with an expected run time of O(n log n)"
insertionSortName = "Insertion Sort with an expected run time of O(n^2)"
selectionSortName = "Selection Sort with an expected run time of O(n^2)"


'''
