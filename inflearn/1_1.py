N, K = list(map(int, input().split()))

count = 0

for idx in range(1, N // 2 + 1):
    if(N % idx == 0):
        count += 1
    
    if count == K:
        print(idx)
        break
else:
    print(-1)