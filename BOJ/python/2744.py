str = input()

for i in range(len(str)):
    if ord(str[i]) > 96:
        print(chr(ord(str[i]) - 32), end="")
    else:
        print(chr(ord(str[i]) + 32), end="")
print("")