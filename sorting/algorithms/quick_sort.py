from .sort import Sort


class QuickSort(Sort):
    def run_sort(self, dataset):
        return self.quickSort(0, len(dataset) - 1)

    def quick_sort(self, lo, hi):
        hi = int(hi)
        lo = int(lo)
        if (hi - lo) < 1:
            return

        j = self.partition(lo, hi)
        self.quickSort(lo, j)
        self.quickSort(j + 1, hi)

    def partition(self, lo, hi, dataset):
        i = lo - 1
        j = hi + 1
        pivot = lo
        exit = False

        while exit == False:
            while i <= hi:
                i = i + 1
                if mylist[i] >= mylist[pivot]:
                    break
            while j >= lo:
                j = j - 1
                if dataset[j] <= dataset[pivot]:
                    if j <= i:
                        exit = True
                        break
                    if i == pivot:
                        pivot = j
                    temp = mylist[i]
                    dataset[i] = dataset[j]
                    dataset[j] = temp
                    break
        return j
