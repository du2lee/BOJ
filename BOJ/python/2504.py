sik = input()
stack = []
cache = 1
answer = 0

for i in range(len(sik)):
    node = sik[i]

    if node == '[':
        cache *= 3
        stack.append(node)
    elif node == '(':
        cache *= 2
        stack.append(node)
    elif node == ']':
        if stack[-1] == '(' or not stack:
            answer = 0
            break
        if sik[i - 1] == '[':
            answer += cache
        cache //= 3
        stack.pop()
    elif node == ')':
        if stack[-1] == '[' or not stack:
            answer = 0
            break
        if sik[i - 1] == '(':
            answer += cache
        cache //= 2
        stack.pop()

print(answer)
