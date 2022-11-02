
import time
import sys
MAX_SIZE = sys.maxsize

############# Bubble Sort #############

def bubble_sort(data, drawrectangle, delay):
    for i in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

                drawrectangle(data, ['blue' if x == j or x == j+1 else 'red' for x in range(len(data))])
                time.sleep(delay)
    drawrectangle(data, ['blue' for x in range(len(data))])


############# Insertion Sort #############

def insertion_sort(data, drawrectangle, delay):
    for i in range(1,len(data)):
        value = data[i]
        j = i
        while value <= data[j-1] and j != 0:
            drawrectangle(data, ['blue' if x == j else 'red' for x in range(len(data))])
            time.sleep(delay)

            data[j],data[j-1] = data[j-1],data[j]
            j -= 1

        drawrectangle(data, ['blue' if x == j else 'red' for x in range(len(data))])
        time.sleep(delay)
    drawrectangle(data, ['blue' for x in range(len(data))])


############# Selection Sort #############

def selection_sort(data, drawrectangle, delay):
    for i in range(len(data)-1):
        pos = i
        last = MAX_SIZE
        for j in range(i+1, len(data)):
            drawrectangle(data, [('lightyellow' if x == j else ('lightblue' if x == i else 'red')) for x in range(len(data))])
            time.sleep(delay)

            if data[j] < data[i] and data[j] < last:
                pos = j
                last = data[j]

        drawrectangle(data, [('blue' if x == pos else ('lightblue' if x == i else 'red')) for x in range(len(data))])
        time.sleep(delay)
        temp = data[i]
        data[i] = data[pos]
        data[pos] = temp

    drawrectangle(data, ['blue' for x in range(len(data))])


############# Merge Sort #############

def merge_sort(data, drawrectangle, delay):
    merge_sort_alg(data, 0, len(data)-1, drawrectangle, delay)

    drawrectangle(data, ['blue' for x in range(len(data))])
    time.sleep(delay)

def merge_sort_alg(data, left, right, drawrectangle, delay):
    if left >= right:
        return
    middle = (left + right)//2

    merge_sort_alg(data, left, middle, drawrectangle, delay)
    merge_sort_alg(data, middle+1, right, drawrectangle, delay)
    merge(data, left, middle, right, drawrectangle, delay)

def merge(data, left, middle, right, drawrectangle, delay):
    drawrectangle(data, ['red' for x in range(len(data))])
    time.sleep(delay)

    leftPart = data[left:middle+1]
    rightPart = data[middle+1:right+1]
    
    leftIdx, rightIdx = 0,0

    for i in range(left, right+1):
        if leftIdx < len(leftPart) and rightIdx < len(rightPart):
            if leftPart[leftIdx] <= rightPart[rightIdx]:
                data[i] = leftPart[leftIdx]
                leftIdx += 1
            else:
                data[i] = rightPart[rightIdx]
                rightIdx += 1
        elif leftIdx < len(leftPart):
            data[i] = leftPart[leftIdx]
            leftIdx += 1
        else:
            data[i] = rightPart[rightIdx]
            rightIdx += 1

        drawrectangle(data, ['lightblue' if x == i else 'red' for x in range(len(data))])
        time.sleep(delay)


############# Quick Sort #############

colordata = []

def partition(data,low,high, drawrectangle, delay):
    i = ( low-1 )
    pivot = data[high]
    for j in range(low , high):
        if data[j] <= pivot:
            i = i+1
            data[i],data[j] = data[j],data[i]

        for x in range(len(colordata)):
            if x == i:
                colordata[x] = '#ff0000'
            elif i < x < high:
                colordata[x] = 'lightyellow'
            elif x == high:
                colordata[x] = 'lightblue'
            else:
                colordata[x] = 'red'

        drawrectangle(data, colordata)
        time.sleep(delay)

    data[i+1],data[high] = data[high],data[i+1]
    return ( i+1 )

def quickSort(data,low,high, drawrectangle, delay):
    if low < high:
        pi = partition(data,low,high, drawrectangle, delay)
        quickSort(data, low, pi-1, drawrectangle, delay)
        quickSort(data, pi+1, high, drawrectangle, delay)

def quick_sort(data, drawrectangle, delay):
    global colordata
    colordata = ['red' for x in range(len(data))]
    quickSort(data, 0, len(data)-1, drawrectangle, delay)
    drawrectangle(data, ['blue' for x in range(len(data))])


############# Heap Sort #############

colordata = []  

def heapify(data, n, i, drawrectangle, delay):
    largest = i
    l = 2*i
    r = 2*i + 1

    if l < n and data[largest] < data[l]:
        largest = l

    if r < n and data[largest] < data[r]:
        largest = r
        
    if largest != i:
        data[i], data[largest] = data[largest], data[i]

        drawrectangle(data, ['lightblue' if x == i or x == largest else colordata[x] for x in range(len(data))])
        time.sleep(delay)

        heapify(data, n, largest, drawrectangle, delay)


def heap_sort(data, drawrectangle, delay):
    global colordata

    colordata = ['red' for x in range(len(data))]

    n = len(data)
    for i in range(n//2 - 1, -1, -1):
        heapify(data, n, i, drawrectangle, delay)
    
    for i in range(n-1, 0, -1):
        data[i], data[0] = data[0], data[i]

        drawrectangle(data, ['lightyellow' if x == i or x == 0 else colordata[x] for x in range(len(data))])
        time.sleep(delay)
        colordata[i] = 'blue'

        heapify(data, i, 0, drawrectangle, delay)

    drawrectangle(data, ['blue' for x in range(len(data))])