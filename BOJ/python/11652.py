N = int(input())
array = dict()

for _ in range(N):
    num = int(input())
    try:
        array[num] += 1
    except:
        array[num] = 1

cache = []
maxValue = max(list(array.values()))

for k, v in array.items():
    if v == maxValue:
        cache.append(k)
print(min(cache))
