from collections import deque

S, E = list(map(int, input().split()))

answer = 0

while S != E:
    d = E - S

    answer += 1

    if d >= 4:
        S += 5
    elif d < 0:
        S -= 1
    else:
        S += 1

print(answer)