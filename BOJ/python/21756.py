N = int(input())
array = []

for i in range(N):
    array.append(i + 1)

while len(array) > 1:
    # condition A
    cache = []
    for i in range(len(array)):
        if i % 2 == 1:
            cache.append(array[i])
    # condition B
    array = cache

print(array[0])