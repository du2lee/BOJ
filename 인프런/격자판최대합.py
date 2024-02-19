import math

N = int(input())
excel = [list(map(int, input().split())) for _ in range(N)]
answer = -math.inf

for row in excel:
    cache = sum(row)
    if answer < cache:
        answer = cache

for column in zip(*excel):
    cache = sum(column)
    if answer < cache:
        answer = cache

cache1 = 0
cache2 = 0
for idx in range(N):
    cache1 += excel[idx][idx]
    cache2 += excel[N - idx - 1][idx]
if answer < cache1:
    answer = max(cache1,cache2)

print(answer)