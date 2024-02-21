from collections import deque

N, M = list(map(int, input().split()))
kgs = list(map(int, input().split()))
kgs.sort(reverse=True)
kgs = deque(kgs)
answer = 0

while kgs:
    a = kgs.popleft()
    if len(kgs) > 0:
        if a + kgs[-1] <= M:
            kgs.pop()
    answer += 1

print(answer)
