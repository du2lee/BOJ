import sys, math
from typing import Counter

N = int(sys.stdin.readline())
value_array = []
sum = 0

for _ in range(N):
    value = int(sys.stdin.readline())
    value_array.append([value, 1])

value_array.sort()

for i in range(len(value_array)):
    sum += value_array[i][0]
    if i != 0 and value_array[i][0] == value_array[i - 1][0]:
        value_array[i][1] += value_array[i - 1][1]

average = round(sum / len(value_array))
medium = value_array[int(len(value_array) // 2)][0]
rangeArray = value_array[len(value_array) - 1][0] - value_array[0][0]


value_array.sort(key=lambda x: (-x[1], x[0]))

if len(value_array) <= 1:
    mode = value_array[0][0]
else:
    if value_array[0][1] == value_array[1][1]:
        mode = value_array[1][0]
    else:
        mode = value_array[0][0]

print(average)
print(medium)
print(mode)
print(rangeArray)