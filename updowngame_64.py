import sys
from math import pow

X = int(sys.stdin.readline())
def func(value, i):
    if value == X:
        print(i)
        return
    half = 64 // pow(2, i + 1)              
    if value < X:
        value += half
    elif value > X:
        value -= half
    print(value)
    func(value, i + 1)

func(64, 0)