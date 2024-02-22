s1 = list(input())
s2 = list(input())

check = {}

for num in range(65, 91):
    check[chr(num)] = 0

for num in range(97, 123):
    check[chr(num)] = 0

for idx in range(len(s1)):
    check[s1[idx]] += 1
    check[s2[idx]] -= 1

for key in check.keys():
    if check[key] != 0:
        print("NO")
        break
else:
    print("YES")
    