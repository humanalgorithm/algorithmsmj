import random

class ArrayBuilder(object):
    def __init__(self):
        pass

    # initializes array of user defined size, currenlty does
    # so in random array size
    def randomize(self, arraysize):
        array_size = int(arraysize)
        tempArray = []

        # assign random values for length of array
        for x in range(0, array_size):
            tempArray.append(random.randint(1, 10000))

        return tempArray

    def arrayToString(object):
        global mylist
        arrayLimit = 35
        str1 = ""
        xholder = 0
        if arrayLimit <= len(mylist):
            arrayLimit = arrayLimit
        if arrayLimit >= len(mylist):
            arrayLimit = len(mylist)

        for x in range(0, arrayLimit):
            xholder = x
            str1 += str(mylist[x])
            if x != len(mylist) - 1:
                str1 += ","
            if xholder >= arrayLimit - 1:
                str1 += "..."

        return str1

    def resetArray(self):
        global lastarray
        global mylist
        global sortName
        global timeElapsed

        sortName = "Please select sort"
        timeElapsed = 0

        if lastRandom == False:
            for x in range(0, len(mylist) - 1):
                mylist[x] = lastarray[x]
