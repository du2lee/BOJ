strings = list()

while True:
    strings = input()
    
    if strings == '.':
        break

    cache = list()
    cache.append(-1)
    stack = list(strings)
    boolean = True
    
    while stack:
        value = stack.pop()
        if value == ')':
            cache.append(')')
        elif value == '(':
            caches = cache.pop()
            if caches == ']' or caches == -1:
                boolean = False
                break
        elif value ==']':
            cache.append(']')
        elif value == '[':
            caches = cache.pop()
            if caches == ')' or caches == -1:
                boolean = False
                break
    cache.pop()        
    if boolean == True:
        print('yes')
    else:
        print('no')