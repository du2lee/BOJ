import sys

T, N = map(int,sys.stdin.readline().split())

cards = [i for i in map(int, sys.stdin.readline().split())]

cards.sort()

sum = 0
count = 0

for i in range(len(cards)):
    if cards[i] >= N:
        break
    count += 1

for i in range(count):
    for j in range(i+1, count):
        for k in range(j+1 , count):
            if cards[i] + cards[j] + cards[k] <= N and cards[i] + cards[j] + cards[k] > sum:
                sum = cards[i] + cards[j] + cards[k]
                if sum == N:
                    print(sum)
                    exit()
print(sum)