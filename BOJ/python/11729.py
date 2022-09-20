N = int(input())

def hanoi(N, a, b, c):
    if N == 1:
        print(a, c)

    else:
        hanoi(N - 1, a, c, b)
        print(a, c)
        hanoi(N - 1, b, a, c)

print(2 ** N - 1)
hanoi(N, 1, 2, 3)










# import sys


# def func(N, a, b, c):
#     if N == 1:
#         print(a, c)
#     else:
#         func(N - 1, a, c, b)
#         print(a, c)
#         func(N - 1, b, a, c)


# N = int(sys.stdin.readline())

# print(pow(2,N) - 1)
# func(N , 1, 2, 3)