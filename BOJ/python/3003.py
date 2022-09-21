arr = list(map(int, input().split()))

king = 1 - arr[0]
queen = 1 - arr[1]
look = 2 - arr[2]
bishop = 2 - arr[3]
knight = 2 - arr[4]
phone = 8 - arr[5]

print(king, queen, look, bishop, knight, phone)
