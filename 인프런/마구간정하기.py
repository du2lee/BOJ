N, C = list(map(int, input().split()))
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()
answer = -1

def Count(km):
    count = 0
    preHorse = - 10e11
    for x in arr:
        if x - preHorse >= km:
            preHorse = x
            count += 1
    return count

def func(s, e):
    global answer
    if s > e:
        return
    
    mid = (s + e) // 2

    if Count(mid) < C:
        func(s, mid - 1)
    else:
        if answer < mid:
            answer = mid
        func(mid + 1, e)
func(1, max(arr))
print(answer)
    