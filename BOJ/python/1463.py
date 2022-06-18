N = int(input())

array = [0] * (N + 1)

for idx in range(2, N + 1):
    array[idx] = array[idx - 1] + 1

    if idx % 3 == 0:
        array[idx] = min(array[idx // 3] + 1, array[idx])
    
    if idx % 2 == 0:
        array[idx] = min(array[idx // 2] + 1, array[idx])
        
print(array[N])