import sys

def a(N):
    count = 0
    for i in range(100, N+1):
        A = int(i //100)
        B = int((i //10) % 10)
        C = int(i % 10)
        if (A-B) == (B-C):
            count += 1
    if N >= 100:
        count += 99
    else:
        count += N
    print(count)


N = int(sys.stdin.readline())
a(N)

##no pass in 백준