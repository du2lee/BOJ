import sys
X = int(sys.stdin.readline())
count = 1
sum = 1
while True:
    if X <= sum:
        if count%2 == 1:
            print((1 + sum - X) , "/" , (count - sum + X),sep= "")
        
        else:
            print((count - sum + X) , "/" , (1 + sum - X),sep= "")
        break
    count += 1
    sum += count