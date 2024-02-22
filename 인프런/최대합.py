import heapq

q = []

while True:
    num = int(input())

    if num == -1:
        break

    if num == 0:
        if len(q) == 0:
            print(-1)
        else:
            print(-heapq.heappop(q))
    else:
        heapq.heappush(q, -num)
