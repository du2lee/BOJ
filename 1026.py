import sys

N = int(sys.stdin.readline())

a_Array = list(i for i in map(int, sys.stdin.readline().split()))
b_Array = list(i for i in map(int, sys.stdin.readline().split()))
a_Array.sort()
b_Array.sort(key= lambda x:-x)

sum = 0

for i in range(N):
    sum += a_Array[i] * b_Array[i]

print(sum)