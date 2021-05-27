import sys

#def count_array(N):
#    count_array = [0 for i in range(10001)]
#    #sum = 0
#    
#    for j in range(N):
#        value = int(sys.stdin.readline())
#        count_array[value - 1] += 1
#    
#    for k in range(10001):
        #if sum == N:             # finish counting
        #    break
        #sum += count_array[k]
#        if count_array[k] != 0:
#            for l in range(count_array[k]):
#                print(k+1)

N = int(sys.stdin.readline())

count_array = [0] * 10001

for _ in range(N):
    value = int(sys.stdin.readline())
    count_array[value - 1] += 1
    
for k in range(10001):
    if count_array[k] != 0:
        for _ in range(count_array[k]):
             print(k+1)


#count_array(N)