import sys
a, b = map(int, sys.stdin.readline().split())
reverse_a = (a // 100) + ((a % 10) * 100) + ((a // 10) % 10) * 10
reverse_b = (b // 100) + ((b % 10) * 100) + ((b // 10) % 10) * 10

if reverse_a >= reverse_b:
    print(reverse_a)
else:
    print(reverse_b)