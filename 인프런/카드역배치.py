cards = [idx for idx in range(0, 21)]

for _ in range(10):
    s, e = list(map(int, input().split()))

    for idx in range((e - s + 1) // 2):
        cards[s + idx], cards[e - idx] = cards[e - idx], cards[s + idx]

for num in cards[1:]:
    print(num, end= " ")
print()