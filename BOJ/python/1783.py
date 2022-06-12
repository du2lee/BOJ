import sys

N ,M = map(int,sys.stdin.readline().split())

if N == 1 or M == 1:
    print(1)
# elif M == 2:
#     print(min(4, int((N - 1) / 2) + 1))           //이거 때문에 엄청 틀림
elif N == 2:
    print(min(4, int((M - 1) / 2) + 1))
elif M < 7:
    print(min(4 , M))
else:
    print(M - 2)