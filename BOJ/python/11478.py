s = input()
arr = set()

i = 0
while i < len(s):
    for idx in range(len(s) - i):
        arr.add(s[idx:idx+i+1])
    i += 1

print(len(arr))