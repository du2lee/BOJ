import sys

N = int(sys.stdin.readline())
array = []
for i in range(N):
    age , name = sys.stdin.readline().split()
    value = (i, int(age), name)
    array.append(value)

array.sort(key=lambda x: (x[1],x[0]))

for person in array:
    print(person[1], person[2])