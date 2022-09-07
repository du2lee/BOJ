import sys

def binarySearch(arr, start, end, value):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] == value:
            return mid
        elif value < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return None

N = int(sys.stdin.readline().rstrip())
arrayN = list(map(int,sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
arrayM = list(map(int, sys.stdin.readline().rstrip().split()))

arrayN.sort()
for i in arrayM:
    cache = binarySearch(arrayN, 0, N, i)
    if cache == None:
        print('No', end = ' ')
    else:
        print('yes', end = ' ')