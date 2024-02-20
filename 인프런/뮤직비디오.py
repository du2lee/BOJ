import math
N, M = list(map(int, input().split()))
times = list(map(int, input().split()))
answer = math.inf
maxValue = max(times)

def Count(HDD):
    count = 1
    sum = 0
    for v in times:
        if sum + v > HDD:
            count += 1
            sum = v
        else:
            sum += v

    return count

def func(s, e):
    global answer
    global maxValue
    if s > e:
        return
    
    mid = (s + e) // 2

    if maxValue <= mid and Count(mid) <= M:
        answer = mid
        func(s, mid - 1)

    else:
        func(mid + 1, e)

func(1, sum(times))
print(answer)