knight = input()

location = [ord(knight[0]) - 96, int(knight[1])]
count = 0

go = [(1,2),(1,-2),(-1,-2),(-1,2),(2,1),(2,-1),(-2,1),(-2,-1)]

for x, y in go:
    if location[0] + x <= 8 and location[0] + x > 0 and location[1] + y <= 8 and location[1] + y > 0:
        count += 1

print(count)
