N = int(input())
getCard = set(map(int, input().split()))

M = int(input())
checkCard = list(map(int, input().split()))

for i in checkCard:
    if i in getCard:
        print(1, end = ' ')
    else:
        print(0, end = ' ')
print()