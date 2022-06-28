inputs = input()
stack= []
count = 0

for idx in range(len(inputs)):
    if inputs[idx] == '(':
        stack.append(idx)
    elif inputs[idx] == ')':
        open = stack.pop()
        if idx - open == 1:
            count += len(stack)
        else:
            count += 1
print(count)