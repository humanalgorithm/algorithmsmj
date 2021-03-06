from .sort import Sort

class InsertionSort(Sort):
    def sort(self, dataset):
        for i in range(1, len(dataset)):
            j = i
            while j >= 1 and dataset[j] < dataset[j - 1]:
                temp = dataset[j - 1]
                dataset[j - 1] = dataset[j]
                dataset[j] = temp
                j = j - 1
        return dataset
