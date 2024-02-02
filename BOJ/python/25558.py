N = int(input())

sx, sy, ex, ey = list(map(int, input().split()))

value = 10e12
answer = 1

for _ in range(N):
    cache = 0
    x, y = sx, sy
    for __ in range(int(input())):
        X, Y = list(map(int, input().split()))
        cache += abs(X - x) + abs(Y - y)
        x, y = X, Y

    cache += abs(ex - x) + abs(ey - y)

    if cache < value:
        value = cache
        answer = _ + 1
        
print(answer)