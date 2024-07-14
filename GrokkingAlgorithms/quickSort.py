def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        more = [i for i in arr[1:] if i > pivot]

        return quickSort(less) + [pivot] + quickSort(more)


print(quickSort([10, 5, 2, 3, 8, 11, 9, 4, 6]))
