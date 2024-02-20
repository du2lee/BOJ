K, N = list(map(int, input().split()))
arr = []
answer = -1

def func(s, e):
    global answer
    if s > e:
        return
    
    mid = (s + e) // 2

    cache = 0
    for v in arr:
        cache += v // mid
    
    if cache < N:
        func(s, mid - 1)
    else:
        if answer < mid:
            answer = mid
        func(mid + 1, e)

for _ in range(K):
    arr.append(int(input()))

func(1, max(arr))

print(answer)


