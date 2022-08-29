N = int(input())
scores = list(map(int, input().split()))

result = max(scores) - min(scores)
print(result)