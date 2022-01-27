import sys

N = int(sys.stdin.readline())

array = []

for _ in range(N):
    
    x, y = map(int , sys.stdin.readline().split())
    value = (x, y)
    array.append(value)

array.sort(key=lambda x :(x[1],x[0]))

for i in range(N):
    print(array[i][0], array[i][1])