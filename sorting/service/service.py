from .factory import SortFactory

class SortService(object):
    def __init__(self, dataset, sort_method):
        self._sort_obj = SortFactory().get_sort_obj(sort_method)
        self._dataset = dataset

    def sort(self):
        return self._sort_obj().run_sort(self._dataset)

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
