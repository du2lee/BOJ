import sys
N = int(sys.stdin.readline())
num = 1
count = 1

while True:
    if N <= num:
        print(count)
        break
    num += (6*count)
    count += 1