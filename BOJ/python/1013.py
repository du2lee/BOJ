import re

for _ in range(int(input())):
    if re.compile("(100+1+|01)+").fullmatch(input()):
        print("YES")
    else:
        print("NO")
