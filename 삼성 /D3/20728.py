from math import inf

for i in range(int(input())):
    answer = inf

    N, K = list(map(int, input().split()))

    pocket = list(map(int, input().split()))

    pocket.sort()

    for idx in range(N - K + 1):
        answer = min(answer, pocket[idx + K - 1] - pocket[idx])

    print("#" + str(i + 1) + " " + str(answer))