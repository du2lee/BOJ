number = input()

arr = [0 for _ in range(10)]

for num in number:
    arr[int(num)] += 1

arr[6] += arr[9]
arr[6] /= 2

result = max(arr[:-1])
if result > int(result):
    print(int(result) + 1)
else:
    print(int(result))