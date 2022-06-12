import sys

gates = int(sys.stdin.readline())
plains = int(sys.stdin.readline())

parent = [i for i in range (gates + 1)]
gates_list = []
count = 0

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

for i in range(plains):
    lines = int(sys.stdin.readline())



    
print(count)