import sys
N = int(sys.stdin.readline())
count =  0
sum = 0
txt = ""
for i in range(N):
    txt = sys.stdin.readline()
    for j in range(len(txt) - 1):
        if txt[j] == 'X':
            count = 0
        else:
            if j != 0 and txt[j-1] == 'O':
                count += 1
            sum += count + 1
    print(sum)
    sum = 0
    count = 0