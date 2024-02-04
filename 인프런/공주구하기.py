from collections import deque

N, K = list(map(int, input().split()))

q = deque()
for i in range(1, N + 1):
    q.append(i)

while len(q) > 1:
    print(q)
    N = len(q)
    mod = K % N

    for _ in range(mod):
        q.append(q.popleft())
    q.pop()

print(q[0])

