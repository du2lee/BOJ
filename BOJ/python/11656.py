N = input()

array = [N]

for idx in range(1, len(N)):
    array.append(N[idx:])

array.sort()

for idx in array:
    print(idx)