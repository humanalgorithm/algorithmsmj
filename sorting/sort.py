#python quicksort program


import random
import time
from multiprocessing import Process, Queue
import threading
import multiprocessing


#intialize global variables
mylist=[]
lastarray=[]
timerStart= 0
timeElapsed = 0
sortName = "Please select sort"
lastRandom = False

bubbleSortName = "Bubble sort with an expected run time of O(N^2)"
quickSortName = "Quick sort with an expected run time of O(n log n)"
mergeSortName = "Merge Sort with an expected run time of O(n log n)"
insertionSortName = "Insertion Sort with an expected run time of O(n^2)"
selectionSortName = "Selection Sort with an expected run time of O(n^2)"

#initializes array of user defined size, currenlty does
#so in random array size
def randomize(arraysize):
    array_size = int(arraysize)
    tempArray = []

     #assign random values for length of array
    for x in range (0, array_size):
     tempArray.append (random.randint(1,10000))

    return tempArray

def arrayToString():
    global mylist
    arrayLimit = 35
    str1 = ""
    xholder = 0
    if arrayLimit <= len(mylist):
        arrayLimit = arrayLimit
    if arrayLimit >= len(mylist):
        arrayLimit = len(mylist)

    for x in range(0,arrayLimit):
        xholder = x
        str1+=str(mylist[x])
        if x!=len(mylist)-1:
            str1+=","
        if xholder >= arrayLimit-1:
            str1+="..."

    return str1

def resetArray():
    global lastarray
    global mylist
    global sortName
    global timeElapsed

    sortName = "Please select sort"
    timeElapsed = 0

    if lastRandom == False:
        for x in range (0, len(mylist)-1):
            mylist[x] = lastarray[x]


def startTimer():
    global timerStart
    timerStart = start_time = time.time()

def setTimeElapsed():
    global timeElapsed
    global timerStart
    timeElapsed = time.time() - timerStart

def quickSortStart(arrayIn, timeout):
    global mylist
    mylist = arrayIn
    startime = time.clock()
    quickSort(0,len(arrayIn)-1, startime, timeout)
    return mylist


def quickSort(lo, hi, starttime,timeout):
    if time.clock() - starttime > timeout+1:
            return 0
    global mylist
    print "in quick at lo:" + str (lo) + " hi:" + str(hi)
    hi = int(hi)
    lo = int(lo)
    if(hi-lo) <1:
        return
    j = partition(lo,hi)

    quickSort(lo, j, starttime, timeout)

    quickSort(j+1,hi,starttime, timeout)

def partition(lo, hi):
    global mylist
    i = lo-1
    j = hi+1
    pivot = lo
    temp = 0

    exit = False

    strarray=""
    for x in range (lo, hi):
        strarray+=str(mylist[x])


    while exit == False:
        while i <= hi:

            i=i+1
            if mylist[i] >= mylist[pivot]:
                break

        while j >= lo:
            j = j - 1
            if mylist[j] <= mylist[pivot]:
                if j <=i:
                    exit = True
                    break
                if i==pivot:
                    pivot = j
                temp = mylist[i]
                mylist[i] = mylist[j]
                mylist[j] = temp
                break
    return j

def representsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def startSelectionSort(listin, timeout):
    starttime = time.clock()
    listin = selectionSort(listin, starttime, timeout)
    return listin

def selectionSort(listIn,starttime,timeout):
    currentLowElementIndex = 0
    j=0
    temp = 0
    swap = False
    for i in range(0,len(listIn)):
        if time.clock() - starttime > timeout+1:
            return listIn
        j=i+1
        currentLowElementIndex = i
        swap = False
        while j<len(listIn):
            if listIn[j] < listIn[currentLowElementIndex]:
                currentLowElementIndex = j
                swap = True
                print "lowest j element is " + str(listIn[j])
            j=j+1

        if swap:
            print "i is " + str(i)
            print "low element is: " + str(listIn[currentLowElementIndex])
            temp = listIn[i]
            listIn[i] = listIn[currentLowElementIndex]
            listIn[currentLowElementIndex] = temp
    return listIn

def startBubbleSort(listin, timeout):
    starttime = time.clock()
    listin = bubbleSort(listin, starttime, timeout)
    return listin

def startInsertionSort(listin,timeout):
    starttime = time.clock()
    listin = insertionSort(listin,starttime, timeout)
    return listin

def insertionSort (listIn, starttime, timeout):
    for i in range(1,len(listIn)):
        print "insertion sort at" + str(listIn[i])
        if time.clock() - starttime > timeout + 1:
            return listIn
        j=i
        while j >=1 and listIn[j] <listIn[j-1]:
            temp = listIn[j-1]
            listIn[j-1] = listIn[j]
            listIn[j] = temp
            j=j-1
    return listIn

def bubbleSort(listIn, starttime, timeout):
    temp = 0
    i = 0
    j=0
    numPasses = len(listIn)
    sorted = False
    while i < numPasses:
        if time.clock() - starttime > timeout+1:
            return listIn
        print "bubble sort at " + str(listIn[i])
        #print "in i loop with i:" + str(i)
        if sorted == True:
            break
        sorted = True
        j=0
        #last i elements will always be sorted
        while j < len(listIn)-1-i:
            #print "in j loop with j:" + str(j)
            if listIn[j] > listIn[j+1]:
                temp = listIn[j+1]
                listIn[j+1] = listIn[j]
                listIn[j] = temp
                sorted = False
            j+=1
        i+=1
    return listIn

def startMergeSort(listin,timeout):
    starttime = time.clock()
    listin = mergeSort(listin, starttime, timeout)
    return listin

def mergeSort(arrayIn, starttime, timeout):
    if time.clock() - starttime > timeout:
        return 0
    leftArrayPass = []
    rightArrayPass = []

    lo = 0
    hi = len(arrayIn)-1
    mid  = (lo + hi)/2
    i=0
    r=mid+1
    print "in merge at " + str(arrayIn[mid])
    while i <= mid:
        leftArrayPass.append(arrayIn[i])
        i=i+1
    while r <= hi:
        rightArrayPass.append(arrayIn[r])
        r=r+1

    #print "left array is: " + str(leftArrayPass)
    #print "right array is: " + str(rightArrayPass)
    if(len(arrayIn))> 1:

        leftArray =	mergeSort(leftArrayPass, starttime, timeout)
        #print "right array is: " + str(rightArrayPass)
        rightArray = mergeSort(rightArrayPass, starttime, timeout)
        arrayReturn = mergeSets(leftArray, rightArray)
        #print "array return is: " + str(arrayReturn)
        return arrayReturn
    else:
        return arrayIn

def mergeSets(leftArray, rightArray):

    returnArray = []

    i=0
    j=0
    k=0
    returnSize = len(leftArray) + len(rightArray)
    for x in range (0, returnSize):
        returnArray.append(0)
    #print "returnArray before: " + str(returnArray)
    while k < returnSize:
        #If I and J not empty compare
        if i<len(leftArray) and j<len(rightArray):
            if leftArray[i]<rightArray[j]:
                returnArray[k] = leftArray[i]
                i+=1
            else:
                returnArray[k] = rightArray[j]
                j+=1
        elif i<len(leftArray) and j>=len(rightArray):
            returnArray[k] = leftArray[i]
            i+=1
        elif i>=len(leftArray) and j<len(rightArray):
            returnArray[k] = rightArray[j]
            j+=1
        elif i>=len(leftArray) and j>=len(rightArray):
            break
        k+=1
    return returnArray

