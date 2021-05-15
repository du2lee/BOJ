import sys

x, y, w, h = map(int,sys.stdin.readline().split())

left = x
right = abs(x - w)
up = abs(y - h)
down = y

value = min(left, right, up, down)
print(value)