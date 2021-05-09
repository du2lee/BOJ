import sys

N = int(sys.stdin.readline())
list_time = []




for i in range(N):
    line = [0, 0]
    line[0], line[1] =  map(int, sys.stdin.readline().split())
    list_time.append(line)

list_time.sort(key=lambda x:(x[1], x[0]))
finish = list_time[0][1]
count = 1

for k in range(1, N):
    if finish <= list_time[k][0]:
        count += 1
        finish = list_time[k][1]     
print(list_time)  
print(count)



#for i in range(N):
#    line = []              # 안쪽 리스트로 사용할 빈 리스트 생성
#    for j in range(2):
#        line.append(0)     # 안쪽 리스트에 0 추가
#    list_time.append(line)

#for j in range(N):
#    list_time[j][0],  list_time[j][1] = map(int, sys.stdin.readline().split())


#list_time.sort(key=lambda x:(x[0], x[1])) ##알고리즘 빅오가 크다.
#max = 0

#for k in range(N):
#    start = list_time[k][0]
#    finish = list_time[k][1]
#    count = 1
#    for l in range(k, N):
#        if finish <= list_time[l][0]:
#            count += 1
#            start = list_time[l][0]
#            finish = list_time[l][1]
#    if max < count:
#        max = count