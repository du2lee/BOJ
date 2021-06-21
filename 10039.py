import sys

array = list(0 for i in range(5))
sum = 0

for i in range(len(array)):
    array[i]= int(sys.stdin.readline())
    if array[i] < 40:
        array[i] = 40
    sum += array[i]
        
avg = sum // len(array)
print(avg)