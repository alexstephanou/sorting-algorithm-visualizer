def countingSort(array, place):
    n = len(array)
    output = [0] * n
    count = [0] * 10

    for i in range(0, n):
        index = array[i] // place
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i-1]

    i = n - 1
    while i >= 0:
        index = array[i] // place
        output[count[index%10]-1] = array[i]
        count[index%10] -= 1
        i -= 1

    for i in range(0, n):
        array[i] = output[i]
        yield array



def radixSort(array):
    maxElement = max(array)
    place = 1

    while maxElement // place > 0:
        n = len(array)
        output = [0] * n
        count = [0] * 10

        for i in range(0, n):
            index = array[i] // place
            count[index%10] += 1

        for i in range(1, 10):
            count[i] += count[i-1]

        i = n - 1
        while i >= 0:
            index = array[i] // place
            output[count[index%10]-1] = array[i]
            count[index%10] -= 1
            i -= 1

        for i in range(0, n):
            array[i] = output[i]
            yield array

        place *= 10
