import sys
A, B, V = map(int, sys.stdin.readline().split())

#days = 1
#s = 0
#while True:            # 시간복잡도 크다
#    s += A
#    if V <= s:
#        print(days)
#        break
#    s -= B
#    days += 1


if (V - A) % (A - B) == 0:
    days = (V - A) / (A - B) 
else:
    days = (V - A) / (A - B) + 1
days += 1
print(int(days))