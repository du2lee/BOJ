num = ''
for s in input():
    if 48 <= ord(s) and 57 >= ord(s):
        num += s
num = int(num)

print(num)

count = 2

for idx in range(2, num // 2 + 1):
    if num % idx == 0:
        count += 1

print(count)
    

