import sys

word = sys.stdin.readline()
list_ahphabet = [0 for i in range(26)]
max = 0
count = 0
output = ""

for j in range(len(word)):
    if ord(word[j]) >= 65 and ord(word[j]) <= 90:
        list_ahphabet[ord(word[j]) - 65] += 1
    elif ord(word[j]) >= 97 and ord(word[j]) <= 122:
        list_ahphabet[ord(word[j]) - 97] += 1

for k in range(26):
    if max < list_ahphabet[k]:
        max = list_ahphabet[k]
        output = chr(k+65)
for l in range(26):
    if max == list_ahphabet[l]:
        count += 1
if count >= 2:
    print("?")
else:
    print(output)