from collections import deque

def func(s):
    if 48 <= ord(s) <= 57 or 97 <= ord(s) <= 122 or 65 <= ord(s) <= 90:
        return True
    return False

S = input()

bufferString = ''
q = deque()
bufferString = ''

for s in S:
    if s == '<':
        print(bufferString, end = '')
        bufferString = ''
        print(s, end = '')
        q.append(s)
    elif s == '>':
        print(s, end = '')
        q.popleft()
    elif s == ' ':
        print(bufferString, end = '')
        bufferString = ''
        print(s, end = '')
    else:
        if len(q) != 0:
            print(s, end = '')
        else:
            bufferString = s + bufferString

if func(S[-1]):
    print(bufferString)