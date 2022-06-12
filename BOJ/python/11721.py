a = input()
output = ''

for idx in range(len(a)):
    output += a[idx]
    if idx == len(a) - 1:
        print(output)
    elif len(output) == 10:
        print(output)
        output = ''