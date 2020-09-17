def mergeSort(array, lb, ub):
    if(ub <= lb):
        return

    elif(lb < ub):
        mid = (lb+ub) // 2
        yield from mergeSort(array, lb, mid)
        yield from mergeSort(array, mid + 1, ub)
        yield from merge(array, lb, mid, ub)
        yield array


def merge(array, lb, mid, ub):
    new = []
    i = lb
    j = mid + 1
    while(i <= mid and j <= ub):
        if(array[i] < array[j]):
            new.append(array[i])
            i += 1
        else:
            new.append(array[j])
            j += 1
    if(i > mid):
        while(j <= ub):
            new.append(array[j])
            j += 1
    else:
        while(i <= mid):
            new.append(array[i])
            i += 1
    for i, val in enumerate(new):
        array[lb + i] = val
        yield array
