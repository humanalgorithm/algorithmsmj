from .sort import Sort

class MergeSort(Sort):
    def sort(self, dataset):
        left_array = []
        right_array = []

        lo = 0
        hi = len(dataset) - 1
        mid = (lo + hi) / 2
        i = 0
        r = mid + 1

        while i <= mid:
            left_array.append(dataset[i])
            i = i + 1
        while r <= hi:
            right_array.append(dataset[r])
            r = r + 1

        if (len(dataset)) > 1:
            left_array = self.sort(left_array)
            right_array = self.sort(right_array)
            dataset_merged = self.merge_sets(left_array, right_array)
            return dataset_merged
        else:
            return dataset

    def merge_sets(self, left_array, right_array):
        return_array = []
        i = 0
        j = 0
        k = 0
        return_size = len(left_array) + len(right_array)
        for x in range(0, return_size):
            return_array.append(0)
        while k < return_size:
            if i < len(left_array) and j < len(right_array):
                if left_array[i] < right_array[j]:
                    return_array[k] = left_array[i]
                    i += 1
                else:
                    return_array[k] = right_array[j]
                    j += 1
            elif i < len(left_array) and j >= len(right_array):
                return_array[k] = left_array[i]
                i += 1
            elif i >= len(left_array) and j < len(right_array):
                return_array[k] = right_array[j]
                j += 1
            elif i >= len(left_array) and j >= len(right_array):
                break
            k += 1
        return return_array