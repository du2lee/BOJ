import sys

array = []

def queue(keyword):
    if keyword == 'pop':
        if len(array) < 1:
            print(-1)
        else:
            print(array[0])
            array.remove(array[0])
    elif keyword == 'size':
        print(len(array))
    elif keyword == 'empty':
        if len(array) < 1:
            print(1)
        else:
            print(0)
    elif keyword == 'front':
        if len(array) < 1:
            print(-1)
        else:
            print(array[0])
    elif keyword == 'back':
        if len(array) < 1:
            print(-1)
        else:
            print(array[-1])

N = int(sys.stdin.readline())

for _ in range(N):
    inputs = sys.stdin.readline().split()

    if len(inputs) > 1:
        array.append(inputs[1])
    else:
        queue(inputs[0])