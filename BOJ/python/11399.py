N = int(input())

arr = list(map(int, input().split()))

arr.sort()

result = 0

for i in range(1, len(arr) + 1):
    result += sum(arr[0: i])

print(result)


 







# import sys
# N = int(sys.stdin.readline())
# sum = 0

# list_time = [i for  i in map(int, sys.stdin.readline().split())]
# list_time.sort()

# for k in range(N + 1):
#     for l in range(k):
#         sum += list_time[l]
# print(sum)