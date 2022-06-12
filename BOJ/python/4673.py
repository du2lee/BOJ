array = set(range(1,10001))
selfNum_array = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    selfNum_array.add(i)

selfNum = sorted(array - selfNum_array)

for i in selfNum:
    print(i)