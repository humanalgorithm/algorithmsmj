
class Sort(object):
    def run_sort(self, dataset, return_dict={}):
       return_dict['result'] = self.sort(dataset)
       return return_dict['result']


class SortQuicksort(object):
    def run_sort(self, dataset, return_dict={}):
       return_dict['result'] = self.sort(lo=0, hi=len(dataset) - 1, dataset=dataset)
       return return_dict['result']