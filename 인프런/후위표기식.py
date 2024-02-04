s = list(input())
stack = []
ans = ''

for c in s:
    if c.isdecimal():
        ans += c
    else:
        if c == '(':
            stack.append(c)
        elif c == '*' or c == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                ans += stack.pop()
            stack.append(c)
        elif c == '+' or c == '-':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop()

while stack:
    ans += stack.pop()

print(ans)