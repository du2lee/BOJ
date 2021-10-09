parent = []

def find(x):
    if parent[x] == x:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def Union(x, y):
    x = find(x)
    y = find(y)
    parent[y] = x
    
for idx in range(5):
    parent.append(idx)


Union(1,4)
Union(2,4)

for idx in range(5):
    print(find(idx), end =  ' ')