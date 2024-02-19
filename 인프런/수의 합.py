N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

# 처음 부터 값이 나올때 까지 반복 - 시간복잡도 N * log(N)
answer = 0
for start in range(len(A)):
    cache = 0
    for end in range(start, len(A)):
        cache += A[start]
        if cache > M:
            break
        elif cache == M:
            answer += 1
print(answer)

# 예제
start = 0
end = 1
total = A[0]
answer = 0
while True:
    if total < M:
        if end < N:
            total += A[end]
            end += 1
        else:
            break
    elif total == M:
        answer += 1
        total -= A[start]
        start += 1
    else:
        total -= A[start]
        start += 1

print(answer)
        
