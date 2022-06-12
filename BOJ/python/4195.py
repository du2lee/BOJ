parent = dict()

def find(x):
    if parent[x][0] == x:
        return x
    else:
        p = parent[x][0]
        parent[x][0] = find(p)
        return parent[x][0]

def Union(x, y):
    num = parent[x][1] + parent[y][1]
    x = find(x)
    y = find(y)
    parent[y][0] = x
    parent[y][1] = num
    parent[x][1] = num
    for idx in parent.keys():
        if parent[idx][0] == y:
            parent[idx][0] = x
            parent[idx][1] = num
            
        elif parent[idx][0] == x:
            parent[idx][1] = num
    print(num)

T  = int(input())

for _ in range(T):
    F = int(input())
    parent = dict()
    for _ in range(F):
        x, y = input().split()
        num = 2
        if x not in parent:
            parent[x] = [x, 1]
        if y not in parent:
            parent[y] = [y, 1]
        Union(x, y)




# parent = dict()

# def find(x):
#     if parent[x] == x:
#         return x
#     else:
#         p = parent[x]
#         parent[x] = find(p)
#         return parent[x]

# def Union(x, y):
#     x = find(x)
#     y = find(y)
#     parent[y] = x
#     for idx in parent.keys():
#         if parent[idx] == y:
#             parent[idx] = x

# T  = int(input())

# for _ in range(T):
#     F = int(input())
#     parent = dict()
#     for _ in range(F):
#         x, y = input().split()
#         num = 2
#         if x not in parent:
#             parent[x] = x
#         if y not in parent:
#             parent[y] = y
#         Union(x, y)
#         print(parent)
