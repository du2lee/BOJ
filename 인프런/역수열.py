from collections import deque

N = int(input())
arr = list(map(int, input().split()))

answer = [0 for _ in range(N)]

def func(idx, num):
    while idx < N:
        if answer[idx] == 0:
            answer[idx] = num
            break
        idx += 1

for idx in range(N):
    count = 0
    value = -1
    
    for i in range(N):
        if count == arr[idx]:
            value = i
            break
        if answer[i] == 0:
            count += 1

    func(value, idx + 1)

for v in answer:
    print(v, end= " ")
    