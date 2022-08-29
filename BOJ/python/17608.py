array = []
N = int(input())
for _ in range(N):
    array.append(int(input()))

count = 0
check = 0

for i in range(len(array), 0, -1):
    if check < array[i - 1]:
        check = array[i - 1]
        count += 1

print(count)