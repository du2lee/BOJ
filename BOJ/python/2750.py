import sys

N = int(sys.stdin.readline())

values = []
for i in range(N):
    value = int(sys.stdin.readline())
    values.append(value)

values_2 = list(set(values))
values_2.sort()

for j in range(len(values_2)):
    print(values_2[j])