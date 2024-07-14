def binarySearch(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == x:
            return mid

        if arr[mid] > x:
            return binarySearch(arr, low, mid - 1, x)

        else:
            return binarySearch(arr, mid + 1, high, x)

    else:
        return None


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 8

print(f"Element {x} in {arr} has index:", binarySearch(arr, 0, len(arr) - 1, x), "\n")
