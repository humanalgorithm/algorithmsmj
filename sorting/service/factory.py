from sorting.algorithms.quick_sort import QuickSort
from sorting.algorithms.merge_sort import MergeSort
from sorting.algorithms.bubble_sort import BubbleSort
from sorting.algorithms.insertion_sort import InsertionSort
from sorting.algorithms.selection_sort import SelectionSort

class SortFactory(object):
    def __init__(self):
        self._sort_map = {"quicksort": QuickSort,
                    "mergesort": MergeSort,
                    "bubblesort": BubbleSort,
                    "insertionsort": InsertionSort,
                    "selectionsort": SelectionSort
                    }

    def get_sort_obj(self, sort_method):
        return self._sort_map.get(sort_method.lower())
