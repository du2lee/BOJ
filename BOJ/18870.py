import sys

N = int(sys.stdin.readline())

value = list(map(int, sys.stdin.readline().split()))

rank = list(set(value))
rank.sort()
dic = {rank[i] : i for i in range(len(rank))}
for i in value:
    print(dic[i], end=' ')