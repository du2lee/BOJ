N = int(input())
arr = list(map(int, input().split()))
findNum = int(input())
count = 0

for i in range(len(arr)):
    if(arr[i] == findNum):
        count += 1

print(count)