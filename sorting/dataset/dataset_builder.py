import random


class DatasetBuilder(object):
    def __init__(self):
        self.rand_int_low = 1
        self.rand_int_high = 10000
        self.max_size = 1000

    def get_random_dataset(self, dataset_size):
        dataset_size = int(dataset_size)
        if dataset_size > self.max_size:
            return -1

        dataset_return = []
        [dataset_return.append(random.randint(self.rand_int_low, self.rand_int_high)) for x in range(0, dataset_size)]
        return dataset_return

    def convert_list_to_string(self, dataset):
        return ', '.join(str(x) for x in dataset)

    def resetArray(self):
        global lastarray
        global mylist
        global sortName
        global timeElapsed

        sortName = "Please select sort"
        timeElapsed = 0
