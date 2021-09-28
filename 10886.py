import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    count_0 = 0
    count_1 = 0
    if N == 1:
        count_1 += 1
    else:
        count_0 += 1

if count_1 >= count_0:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")