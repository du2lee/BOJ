import sys


def func(value, A, I):
    if value / A < I - 1:
        print(value + 2)
        return
    func(value - 1, A, I)
    

if __name__ == "__main__":
    A, I = map(int, sys.stdin.readline().split())

    func(A * I, A, I)