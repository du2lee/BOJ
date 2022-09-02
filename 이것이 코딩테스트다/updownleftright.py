N = int(input())

location = [1,1]
move = input().split()

for i in move:
    if i == 'R' and location[0] < N:
        location[0] += 1
    elif i == 'L' and location[0] > 1:
        location[0] -= 1
    elif i == 'D' and location[1] < N:
        location[1] += 1
    elif i == 'U' and location[1] > 1:
        location[1] -= 1

print(location[1], location[0])
