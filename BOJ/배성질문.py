from itertools import combinations

T = int(input())

for i in range(T):
    N, M = list(map(int, input().split()))

    # input edge
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    
    countTri = 0
    # count Triangle
    for edge in combinations(edges, 3):
        nodes = set()
        for node1, node2 in edge:
            nodes.add(node1)
            nodes.add(node2)
        
        if len(nodes) == 3:
            countTri += 1

    print('#{} {}'.format(i+1, countTri))
