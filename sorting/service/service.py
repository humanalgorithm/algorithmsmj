from .factory import SortFactory

class SortService(object):
    def __init__(self, sort_method):
        self._sort_obj = SortFactory().get_sort_obj(sort_method)

    def get_sort_func(self):
        return self._sort_obj().run_sort