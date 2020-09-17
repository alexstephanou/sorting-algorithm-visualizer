def quickSort(array, l, r):
    if l >= r:
        return
    x = array[l]
    j = l
    for i in range(l+1, r+1):
        if array[i]<=x:
            j+=1
            array[j], array[i] = array[i], array[j]
        yield array
    array[l], array[j]=array[j], array[l]
    yield array
    yield from quickSort(array, l, j-1)
    yield from quickSort(array, j+1, r)
