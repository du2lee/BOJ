S = list(input())
T = list(input())

while len(S) < len(T):
    cache = T.pop()

    if cache == 'B':
        T = list(reversed(T))

if S == T:
    print(1)
else:
    print(0)
