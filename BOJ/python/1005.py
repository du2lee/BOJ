from collections import deque

for _ in range(int(input())):
    N, K = list(map(int, input().split()))
    D = [0] + list(map(int, input().split()))
    degree = [0 for _ in range(N + 1)]
    times = [-1 for _ in range(N + 1)]
    tech = {}

    for idx in range(N + 1):
        tech[idx] = []

    for _ in range(K):
        s, e = list(map(int, input().split()))
        tech[s].append(e)
        degree[e] += 1

    q = deque()

    for idx in range(1, N + 1):
        if degree[idx] == 0:
            times[idx] = D[idx]
            q.append((idx, D[idx]))

    while q:
        sn, time = q.popleft()

        for en in tech[sn]:
            degree[en] -= 1
            times[en] = max(times[en], time + D[en])
            if degree[en] == 0:
                q.append((en, times[en]))

    print(times[int(input())])