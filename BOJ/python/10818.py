# import sys
# N = int(sys.stdin.readline())
# list_N = list(map(int, sys.stdin.readline().split()))
# max = list_N[0]
# min = list_N[0]
# for i in range(N):
#     if list_N[i] > max:
#         max = list_N[i]
#     if list_N[i] < min:
#         min = list_N[i]

# print(min, max)


N = int(input())

array = list(map(int,input().split()))
array.sort()
print(array[0], array[-1])