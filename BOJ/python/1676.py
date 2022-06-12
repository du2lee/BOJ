import sys
from math import factorial

N = int(sys.stdin.readline())
value = factorial(N)
value = str(value)
value_list = list(value)
value_list.reverse()

for i in range(len(value_list)):
    if value_list[i] != '0':
        print(i)
        break