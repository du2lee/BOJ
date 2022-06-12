import sys

words = sys.stdin.readline()
count = 1

for i in range(len(words)):
    if words[i] == " " and i != 0:
        count += 1
if words[len(words)-2] == " ":
    print(count-1)
else:
    print(count)