import sys
N = int(sys.stdin.readline())
max = 0
sum = 0
list_score = [int(x) for x in sys.stdin.readline().split()]
for i in range(N):
    if max < list_score[i]:
        max = list_score[i]
for j in range(N):
    list_score[j] = list_score[j] * 100 / max
    sum += list_score[j]
print(sum / N)