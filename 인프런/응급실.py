from collections import deque

N, M = list(map(int, input().split()))
q = deque(map(int, input().split()))
checkQ = deque()
for i in range(N):
    if i == M:
        checkQ.append(False)
    else:
        checkQ.append(True)

flag = True
ans = 0

while flag:
    ans += 1
    v = max(q)

    while True:
        a = q.popleft()
        b = checkQ.popleft()
        if a == v:
            flag = b
            break
        q.append(a)
        checkQ.append(b)

print(ans)