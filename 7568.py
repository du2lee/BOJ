import sys



N = int(sys.stdin.readline())

people = []

for i in range(N):
    w, h = map(int,sys.stdin.readline().split())
    people.append((w, h))
    
for i in people:
    rank = 1

    for j in people:

        if i != j:
            if i[0]<j[0] and i[1]<j[1]:
                rank += 1
    print(rank, end=' ')
