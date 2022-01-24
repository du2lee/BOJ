import sys

N = int(sys.stdin.readline())
plus =[]
minus = []
countZero = 0
total = 0

for idx in range(N):

    inputNum = int(sys.stdin.readline())
    if inputNum > 0:
        plus.append(inputNum)
    elif inputNum < 0:
        minus.append(inputNum)
    else:
        countZero += 1


plus.sort()
minus.sort(reverse=True)

while len(plus) > 1 :
    a = plus.pop()
    b = plus.pop()
    if a == 1 or b == 1:
        total += a * b + 1
    else:
        total += a * b

while len(minus) > 1:
    c = minus.pop()
    d = minus.pop()
    total += c * d

if len(minus) == 1 and countZero > 0:
    minus.pop()

print(sum(plus) + sum(minus) + total)