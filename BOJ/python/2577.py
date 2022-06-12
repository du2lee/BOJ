import sys
import math
list_input = list()
mul = 1
list_count = [0,0,0,0,0,0,0,0,0,0]
a = False

for i in range(3):
    list_input.append(int(sys.stdin.readline()))
    mul *= list_input[i]
for j in range(9):
    cache = int(mul / int(math.pow(10 , 9-j)))
    mul %= int(math.pow(10 , 9-j))
    if a == False:
        if cache != 0:
            a = True
            list_count[cache] += 1
    else:
        list_count[cache] += 1
list_count[mul] += 1
for j in range(10):
    print(list_count[j])