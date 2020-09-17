def selectionSort(array):
    n = len(array)
    if n == 1:
        return

    for i in range(n):
        minValue = array[i]
        minIndex = i

        for j in range(i, n):

            if array[j] < minValue:
                minValue = array[j]
                minIndex = j
            yield array

        if i != minIndex:
            array[i], array[minIndex] = array[minIndex], array[i]
            
        yield array
