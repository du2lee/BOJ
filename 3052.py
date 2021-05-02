import sys
list_input = list()
list_mod = list()
list_count = list()
sum = 0
for i in range(42):
    list_count.append(False)
for j in range(10):
    list_input.append(int(sys.stdin.readline()))
    list_mod.append(list_input[j] % 42)
    list_count[list_mod[j]] = True
for k in range(42):
    if list_count[k] == True:
        sum += 1
print(sum)