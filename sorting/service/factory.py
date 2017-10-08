from sorting.algorithms.quick_sort import QuickSort
from sorting.algorithms.merge_sort import MergeSort
from sorting.algorithms.bubble_sort import BubbleSort
from sorting.algorithms.insertion_sort import InsertionSort
from sorting.algorithms.selection_sort import SelectionSort

class SortFactory(object):
    def __init__(self, sort_method):
        sort_map = {"quicksort": QuickSort,
                    "mergesort": MergeSort,
                    "bubblesort": BubbleSort,
                    "insertionsort": InsertionSort,
                    "selectionsort": SelectionSort

                    }
        return sort_map.get(sort_method.lower())
