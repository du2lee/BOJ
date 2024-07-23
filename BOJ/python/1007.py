from itertools import combinations
import math

for _ in range(int(input())):
    N = int(input())
    x_all = 0
    y_all = 0

    arr = []
    ans = math.inf

    for __ in range(N):
        x, y = list(map(int, input().split()))
        arr.append((x, y))
        x_all += x
        y_all += y

    for combination in combinations(arr, N // 2):
        x_half = 0
        y_half = 0

        for x, y in combination:
            x_half += x
            y_half += y

        x_sum = x_all - (2 * x_half)
        y_sum = y_all - (2 * y_half)

        vec_sum = ((x_sum ** 2) + (y_sum ** 2)) ** (1/2)

        if ans >= vec_sum:
            ans = vec_sum
    
    print(ans)