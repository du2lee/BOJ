# import sys

# N = int(sys.stdin.readline())
# array = []
# for i in range(N):
#     age , name = sys.stdin.readline().split()
#     value = (i, int(age), name)
#     array.append(value)

# array.sort(key=lambda x: (x[1],x[0]))

# for person in array:
#     print(person[1], person[2])


N = int(input())
array = [0] * N

for idx in range(N):
    array[idx] = list(map(str, input().split()))

array.sort(key= lambda x:(x[0]))

for idx in array:
    print(idx[0], idx[1])