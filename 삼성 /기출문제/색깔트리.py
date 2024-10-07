from collections import deque

N = 100001
# 부모번호, 색, 최대길이, 점수
tree = [[-1, -1, -1]] * N
# 자식번호 저장
children = [[] for _ in range(N)]
# 루트노드 초기화
root = []

for _ in range(int(input())):
    command = list(map(int, input().split()))
    
    if command[0] == 100:
        # 노드추가(고유, 부모, 색깔, 깊이)
        a, b, c, d = command[1], command[2], command[3], command[4]
        # 깊이 비교
        count = 2
        flag = True
        q = deque()

        if b != -1:
            q.append(b)
        while q:
            node = q.popleft()
            
            parent, color, depth = tree[node]
            if depth - count < 0:
                flag = False
                break
            
            if parent != -1:
                q.append(parent)
                count += 1
        # 노드추가
        if flag:
            tree[a] = [b, c, d]
            if b == -1:
                root.append(a)
            else:
                children[b].append(a)
    elif command[0] == 200:
        # 색깔변경
        a, b = command[1], command[2]
        q = deque([a])
        while q:
            node = q.popleft()
            for child in children[node]:
                q.append(child)
            tree[node][1] = b
    elif command[0] == 300:
        # 색깔 조회
        print(tree[command[1]][1])
    elif command[0] == 400:
        # 점수 조회
        answer = 0

        for node in range(1, N):
            if tree[node][0] == -1 and tree[node][1] == -1 and tree[node][2] == -1:
                continue
            arr = [False, False, False, False, False, False]
            arr[tree[node][1]] = True
            cache = 0

            q = deque([node])

            while q:
                n = q.popleft()
                for child in children[n]:
                    q.append(child)
                    arr[tree[child][1]] = True

            for flag in arr:
                if flag:
                    cache += 1
            
            answer += cache * cache
        print(answer)