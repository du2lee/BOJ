import sys

Top = int(sys.stdin.readline())
Middle = int(sys.stdin.readline())
bottom = int(sys.stdin.readline())
coke = int(sys.stdin.readline())
splite = int(sys.stdin.readline())

min_Bugger = min(Top, Middle, bottom)
min_drink = min(coke, splite)

cost = min_Bugger + min_drink - 50

print(cost)