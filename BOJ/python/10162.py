T = int(input())

if T % 10 != 0:
    print(-1)
else:
    a = T // 300
    T %= 300
    b = T // 60
    c = T % 60
    print(a, b, c // 10)