L = int(input())
h = list(map(int, input().split()))
h.sort(reverse = True)

for _ in range(int(input())):
    h[0] -= 1
    h[-1] += 1
    h.sort(reverse=True)

print(h[0] - h[-1])