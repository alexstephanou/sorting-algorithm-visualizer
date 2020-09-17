def insertionSort(array):
    n = len(array)
    for i in range(1, n):
        j = i
        while j > 0 and array[j] < array[j-1]:
            if j != j-1:
                array[j], array[j-1] = array[j-1], array[j]
            j -= 1
            yield array
