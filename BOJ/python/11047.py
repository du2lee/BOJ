from collections import deque
N, money = list(map(int, input().split()))

coins = deque()
count = 0

for _ in range(N):
    coins.appendleft(int(input()))

for i in coins:
    count += money // i
    money %= i 

print(count)