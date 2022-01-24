import sys
list_input = list()
for i in range(9):
    list_input.append(int(sys.stdin.readline()))
max = list_input[0]
index = 0
for j in range(9):
    if max < list_input[j]:
        max = list_input[j]
        index = j + 1
print(max)
print(index)