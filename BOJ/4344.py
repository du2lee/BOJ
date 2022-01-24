import sys
C = int(sys.stdin.readline())
avg = 0
sum = 0
count = 0
for i in range(C):
    list_input = [int(x) for x in sys.stdin.readline().split()]
    for j in range(1, list_input[0] + 1):
        sum += list_input[j]
    avg = sum / list_input[0]
    for k in range(1, list_input[0] + 1):
        if avg < list_input[k]:
            count += 1
    print('%.3f' % (count*100/list_input[0]),"%",sep="")
    sum = 0
    count = 0
    avg = 0