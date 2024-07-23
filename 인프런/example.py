# arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# arr_90 = list(map(list, zip(*arr[::-1])))

# print(arr_90)

# arr_180 = []

# for i in range(len(arr) -1, -1, -1):
#     arr_180.append(arr[i][::-1])

# print(arr_180)


# arr_270 = []

# for i in range(len(arr_90) -1, -1, -1):
#     arr_270.append(arr_90[i][::-1])

# print(arr_270)





arr = [[7 * j + i for i in range(1, 8)] for j in range(7)]
new_arr = [[0] * 7 for _ in range(7)]
sy, sx = 2, 2
length = 3

def lotate_90(sx, sy, l):

    for x in range(sx, sx + l):
        for y in range(sy, sy + l):
            ox, oy = x - sx, y - sy
            lx, ly = oy, l - 1 - ox
            new_arr[lx + sx][ly + sy] = arr[x][y]

    for x in range(sx, sx + l):
        for y in range(sy, sy + l):
            arr[x][y] = new_arr[x][y]

lotate_90(2, 2, 3)
for i in range(len(arr)):
    print(arr[i])