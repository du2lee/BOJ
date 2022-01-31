#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    flag = True
    arr = []
    for idx in s:
        if flag:
            if idx == ' ':
                arr.append(idx)
                continue
            flag = False
            if 97 <= ord(idx) and ord(idx) <= 122:
                arr.append(chr(ord(idx) -32))
            else:
                arr.append(idx)
        elif idx == ' ':
            flag = True
            arr.append(idx)
        else:
            arr.append(idx)
    return ''.join(arr)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
