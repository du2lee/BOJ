numbers = int(input())

answer = 0
array = []
while(True):
    array.append(numbers % 10)
    numbers //= 10
    if numbers == 10:
        array.append(0)
        array.append(1)
        break
    elif numbers // 10 < 10:
        array.append(int(numbers / 10))
        break

print(array)