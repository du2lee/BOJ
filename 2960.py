import sys

count = 0

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    flags = [False, False] + [True] * (N - 1)
    for i in range(2, N + 1):
        if flags[i]:
            count += 1
            if count == K:
                print(i)
                exit()
            for j in range(2 * i, N + 1, i):
                if flags[j] == False:
                    continue
                flags[j] = False
                count += 1
                if count == K:
                    print(j)
                    exit()