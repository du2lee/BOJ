import sys

N = int(sys.stdin.readline())
stack = list()
result = list()
count = 1
boolean = True

for _ in range(1, N + 1):
    cache = int(sys.stdin.readline())
    while count <= cache:
        stack.append(count)
        count += 1
        result.append('+')
    if cache == stack[-1]:
        stack.pop()
        result.append('-')
    else:
        boolean = False
        break

if boolean == False:
    print('NO')
else:
    while result:
        print(result.pop(0))
