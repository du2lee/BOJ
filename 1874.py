import sys

# N = int(sys.stdin.readline())
# stack = list()
# result = list()
# count = 1
# boolean = True

# for _ in range(1, N + 1):
#     cache = int(sys.stdin.readline())
#     while count <= cache:
#         stack.append(count)
#         count += 1
#         result.append('+')
#     if cache == stack[-1]:
#         stack.pop()
#         result.append('-')
#     else:
#         boolean = False
#         break

# if boolean == False:
#     print('NO')
# else:
#     while result:
#         print(result.pop(0))


n = int(sys.stdin.readline())

stack = []
result = []
push = 1
flag = True

for _ in range(n):
    input = int(sys.stdin.readline())
    while push <= input:
        stack.append(push)
        push += 1
        result.append('+')
    if stack[-1] == input:
        stack.pop()
        result.append('-')
    else:
        flag = False
        break
if flag:
    for i in result:
        print(i)
else:
    print('NO')