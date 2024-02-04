expression = list(input())

layer = []
stick = []
cache = []

for i in range(len(expression)):
    now = expression[i]

    if now == '(':
        cache.append((now, i))

    else:
        prev = cache.pop()
        if prev[0] == ')':
            print('식이 틀렸습니다.')
            break

        if prev[1] == i - 1:
            layer.append((prev[1], i))
        else:
            stick.append((prev[1], i))

ans = 0

for s, e in stick:
    for i, j in layer:
        if s >= i or e <= j:
            continue
        ans += 1
    ans += 1

print(ans)







