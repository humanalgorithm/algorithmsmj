from .sort import Sort

class BubbleSort(Sort):
    def sort(self, dataset):
        i = 0
        numPasses = len(dataset)
        sorted = False
        while i < numPasses:
            if sorted == True:
                break
            sorted = True
            j = 0
            # last i elements will always be sorted
            while j < len(dataset) - 1 - i:
                if dataset[j] > dataset[j + 1]:
                    temp = dataset[j + 1]
                    dataset[j + 1] = dataset[j]
                    dataset[j] = temp
                    sorted = False
                j += 1
            i += 1
        return dataset