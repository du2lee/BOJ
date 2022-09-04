A, P = list(map(int, input().split()))

array = [A]

while True:
    A = list(str(A))
    count = 0

    for i in A:
        count += int(i) ** P

    if count in array:
        print(array.index(count))
        break
    array.append(count)
    A = count