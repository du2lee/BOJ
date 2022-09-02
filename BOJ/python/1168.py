import sys

N, K = list(map(int, sys.stdin.readline().split()))

array = [idx for idx in range(1, N + 1)]
answer = []
cursor = -1
while len(array) > 0:
    cursor += K
    cursor %= len(array)
    answer.append(str(array.pop(cursor)))
    cursor -= 1
s = '<' + ', '.join(answer) + '>'
print(s)