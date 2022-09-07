# recursion
def binarySearch(arr, start, end, value):
    if start > end:
        return None
    mid = (start + end) // 2
    if mid == value:
        return mid
    elif mid < value:
        return binarySearch(arr, mid + 1, end, value)
    else:
        return binarySearch(arr, start, mid - 1, value)
    

# loop
def binarySearch(arr, start, end, value):
    while start > end:
        mid = (start + end) // 2
        if mid == value:
            return mid
        elif mid < value:
            start = mid + 1
        elif mid > value:
            end = mid - 1
    return None