def init(tree, node, start, end):   # 세그먼트 트리 초기화
    if start == end:
        tree[node] = 1
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(tree, node * 2, start, mid) + init(tree, node * 2 + 1, mid + 1, end)
    return tree[node]

def update(tree, node, start, end, diff):   # 세그먼트 트리 값 제거
    tree[node] -= 1
    if start == end:
        return 0
    else:
        mid = (start + end) // 2
        if mid < diff:
            return update(tree, node * 2 + 1, mid + 1, end, diff)
        else:
            return update(tree, node * 2, start, mid, diff)
        
def output(tree, node, start, end, diff):   # 세그먼트 트리 값 읽기
    if start == end:
        return start
    mid = (start + end) // 2
    if diff <= tree[node * 2]:
        return output(tree, node * 2, start, mid, diff)
    else:
        return output(tree, node * 2 + 1, mid + 1, end, diff - tree[node * 2])
        
n, k = list(map(int, input().split()))
tree = [0]* 4000000
init(tree, 1, 1, n)
idx = 1
result = []

for i in range(n):
    size = tree[1]
    idx  += k - 1

    if idx % size == 0:
        idx = size
    elif idx > size:
        idx %= size

    num = output(tree, 1, 1, n, idx)
    update(tree, 1, 1, n, num)
    result.append(str(num))

print('<'+', '.join(result)+'>')

########### deque로 푸는 방법 ##############
# from collections import deque

# N, K = list(map(int, input().split()))
# queue = deque([str(i) for i in range(1, N + 1)])
# result = []

# while queue:
#     queue.rotate(-K + 1)
#     result.append(queue.popleft())

# print('<' + ', '.join(result) + '>')