import sys
from collections import deque

def push(stack, value):
    stack.append(value)
def pop(stack):
    if size(stack) <= 0:
        return -1
    return stack.popleft()
def size(stack):
    return len(stack)
def empty(stack):
    if size(stack) <= 0:
        return 1
    return 0
def front(stack): 
    if size(stack) <= 0:
        return -1
    return stack[0]
def back(stack):
    if size(stack) <= 0:
        return -1
    return stack[-1]


stack = deque()
N = int(sys.stdin.readline())

for _ in range(N):
    cache = input().split()
    if cache[0] == 'push':
        push(stack,int(cache[1]))
    elif cache[0] == 'pop':
        value = pop(stack)
        print(value)
    elif cache[0] == 'size':
        value = size(stack)
        print(value)
    elif cache[0] == 'empty':
        value = empty(stack)
        print(value)
    elif cache[0] == 'front':
        value = front(stack)
        print(value)
    elif cache[0] == 'back':
        value = back(stack)
        print(value)





'''import sys
from collections import deque
n = int(sys.stdin.readline())
q = deque([])
for i in range(n):
    s = sys.stdin.readline().split()
    if s[0] == 'push':
        q.append(s[1])
    elif s[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif s[0] == 'size':
        print(len(q))
    elif s[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif s[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif s[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])'''