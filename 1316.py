import sys
N = int(sys.stdin.readline())
count = 0

for i in range(N):
    input_Str = sys.stdin.readline()
    list_count = [False for j in range(26)]
    for k in range(len(input_Str) - 1):
        if list_count[ord(input_Str[k]) - 97] == True and input_Str[k-1] != input_Str[k]:
            count -= 1
            break
        else:
            list_count[ord(input_Str[k]) - 97] = True
    count += 1
print(count)