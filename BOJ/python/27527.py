from collections import deque

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

value = M * 0.9
flag = False

array = []
for _ in range(1000000):
    array.append(deque())

dp = [(A[0], 1)]
array[A[0]].append(0)

if value <= 1:
    flag = True

if N >= 2:
    if A[0] == A[1]:
        if value <= 2:
            flag = True
        dp.append((A[1], 2))
    else:
        dp.append((A[1], 1))
    array[A[1]].append(1)

if N > 2:

    for idx in range(2, N):
        a = 0
        b = 0

        array[A[idx]].append(idx)

        if dp[idx - 1][0] == A[idx]:
            cache = 0
            while True:
                if idx - array[A[idx]][0] <= M:
                    break
                array[A[idx]].popleft()
                cache += 1

            a = dp[idx - 1][1] + 1 - cache

        if dp[idx - 2][0] == A[idx]:
            cache = 0
            while True:
                if idx - array[A[idx]][0] <= M:
                    break
                array[A[idx]].popleft()
                cache += 1

            b = dp[idx - 2][1] + 1 - cache

        if a >= b:
            dp.append((A[idx], a))
        else:
            dp.append((A[idx], b))

        if a >= value or b >= value:
            flag = True
            break

if flag:
    print('YES')
else:
    print('NO')