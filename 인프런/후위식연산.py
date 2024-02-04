s = input()
stack = []

for c in s:
    if c.isdecimal():
        stack.append(c)
    else:
        a = int(stack.pop())
        b = int(stack.pop())
        
        if c == '+':
            stack.append(b+a)
        elif c == '-':
            stack.append(b-a)
        elif c == '*':
            stack.append(b*a)
        elif c == '/':
            stack.append(b/a)

print(int(stack[-1]))
