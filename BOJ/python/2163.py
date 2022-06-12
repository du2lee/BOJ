import sys

n, m = map(int,sys.stdin.readline().split())

count = n - 1
count += n * (m - 1)

print(count)