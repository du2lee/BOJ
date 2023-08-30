str = input()
flag = True

for i in range(len(str) // 2):
    if(str[i] != str[-i -1]):
        flag = False

if flag:
    print(1)
else:
    print(0)