from .sort import SortQuicksort


class QuickSort(SortQuicksort):
    def sort(self, lo, hi, dataset):
        if (hi - lo) < 1:
            return

        j = self.partition(lo, hi, dataset)
        self.sort(lo, j, dataset)
        self.sort(j + 1, hi, dataset)

        return dataset

    def partition(self, lo, hi, dataset):
        i = lo - 1
        j = hi + 1
        pivot = lo
        exit = False

        while exit == False:
            while i <= hi:
                i += 1
                if dataset[i] >= dataset[pivot]:
                    break

            while j >= lo:
                j -= 1
                if dataset[j] <= dataset[pivot]:
                    if j <= i:
                        exit = True
                        break
                    if i == pivot:
                        pivot = j
                    temp = dataset[i]
                    dataset[i] = dataset[j]
                    dataset[j] = temp
                    break
        return j
