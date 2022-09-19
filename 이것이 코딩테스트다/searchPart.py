import sys

def binarySearch(array, start, end, value):
    while start < end:
        mid = (start + end) // 2
        if array[mid] == value:
            return True
        elif array[mid] > value:
            end = mid - 1
        else:
            start = mid + 1
    return False


N = int(sys.stdin.readline())

array = list(map(int, sys.stdin.readline().rstrip().split()))

M = int(sys.stdin.readline())

searchArr = list(map(int, sys.stdin.readline().rstrip().split()))

array.sort()
for i in searchArr:
    if binarySearch(array, 0, N, i):
        print('yes')
    else:
        print('no')






# import sys

# def binarySearch(arr, start, end, value):
#     while start < end:
#         mid = (start + end) // 2
#         if arr[mid] == value:
#             return mid
#         elif value < arr[mid]:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None

# N = int(sys.stdin.readline().rstrip())
# arrayN = list(map(int,sys.stdin.readline().rstrip().split()))
# M = int(sys.stdin.readline().rstrip())
# arrayM = list(map(int, sys.stdin.readline().rstrip().split()))

# arrayN.sort()
# for i in arrayM:
#     cache = binarySearch(arrayN, 0, N, i)
#     if cache == None:
#         print('No', end = ' ')
#     else:
#         print('yes', end = ' ')