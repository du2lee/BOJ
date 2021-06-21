import sys

max = 0
people = 0

for _ in range(4):
    getOut, getIn = map(int, sys.stdin.readline().split())
    people -= getOut
    people += getIn
    if max < people:
        max = people
print(max)
