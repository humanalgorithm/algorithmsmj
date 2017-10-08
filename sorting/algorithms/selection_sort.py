from .sort import Sort

class SelectionSort(Sort):
    def run_sort(self, dataset):
        return self.selectionSort(dataset)

    def selection_sort(self, dataset):
        for i in range(0, len(dataset)):
            j=i+1
            currentLowElementIndex = i
            swap = False
            while j<len(dataset):
                if dataset[j] < dataset[currentLowElementIndex]:
                    currentLowElementIndex = j
                    swap = True
                j=j+1
            if swap:
                temp = dataset[i]
                dataset[i] = dataset[currentLowElementIndex]
                dataset[currentLowElementIndex] = temp
        return dataset
