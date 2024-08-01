from collections import deque

for i in range(int(input())):
    answer = []
    N = int(input())
    cost = list(map(int, input().split()))
    check = dict()

    for v in cost:
        check[v] = deque()

    for idx in range(len(cost)):
        check[cost[idx]].append(idx)

    for idx in range(N * 2):
        if len(answer) >= N:
            break

        v = cost[idx]
        if len(check[v]) == 0:
            continue

        sIdx = check[v].popleft()

        if sIdx != idx:
            check[v].appendleft(sIdx)
            continue

        check[(v // 3) * 4].popleft()
        answer.append(str(v))

    print("#" + str(i + 1), end = " ")
    for v in answer:
        print(v, end = " ")
    print()