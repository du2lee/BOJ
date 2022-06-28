import sys

left = list(sys.stdin.readline().rstrip())
right = []

for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == 'L':
        if len(left) > 0:
            right.append(left.pop())
    elif command[0] == 'D':
        if len(right) > 0:
            left.append(right.pop())
    elif command[0] == 'B':
        if len(left) > 0:
            left.pop()
    elif command[0] == 'P':
        left.append(command[1])

right.reverse()
s = left + right
print(''.join(s))