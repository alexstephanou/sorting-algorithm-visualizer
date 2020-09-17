def heapify(array, index, heapSize):
    largest = index
    leftIndex = 2 * index + 1
    rightIndex = 2 * index + 2
    if leftIndex < heapSize and array[leftIndex] > array[largest]:
        largest = leftIndex

    if rightIndex < heapSize and array[rightIndex] > array[largest]:
        largest = rightIndex

    if largest != index:
        array[largest], array[index] = array[index], array[largest]
        heapify(array, largest, heapSize)


def heapSort(array):
    n = len(array)
    for i in range(n//2-1, -1, -1):
        heapify(array, i, n)
        yield array
    for i in range(n-1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, 0, i)
        yield array
