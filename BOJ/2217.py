import sys

N = int(sys.stdin.readline())
weight = list()
max = 0
for _ in range(N):
    W = int(sys.stdin.readline())
    weight.append(W)
weight.sort(key=lambda x:-x)

for i in range(len(weight)):
    weight[i] = weight[i] * (i + 1)
    if max < weight[i]:
        max = weight[i]
print(max)