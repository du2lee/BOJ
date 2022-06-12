import sys

if __name__ == "__main__":
    H, M = map(int, sys.stdin.readline().split())
    C = int(sys.stdin.readline())

    cache = M + C
    rH = cache // 60 + H
    rM = cache % 60

    if rH > 23:
        rH -= 24

    print(rH, rM)