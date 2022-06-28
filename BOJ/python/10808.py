s = input()

array = [0] * 26

for idx in s:
    array[ord(idx)-97] += 1

for idx in array:
    print(idx, end=" ")