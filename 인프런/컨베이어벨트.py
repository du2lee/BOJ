import math
from copy import deepcopy

needs = list(map(int, input().split()))
M = int(input())
belt = list(map(int, input().split()))

check = {}

for idx in range(10):
    check[idx] = 0

for key in needs:
    check[key] += 1



count = math.inf

for i in range(M):
    cache = deepcopy(check)

    # 한바퀴 돌리기

    if(cache[belt[i]] > 0):
        cache[belt[i]] -= 1
    else:
        cache[0] -= 1
    
    
