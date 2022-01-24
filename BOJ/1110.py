import sys
count = 0 
Num = int(sys.stdin.readline())
orign_Num = Num
while True:
    Num = int((int(Num % 10) + int(Num / 10))%10) + int((Num % 10) * 10)
    count += 1
    if Num == orign_Num:
        break
print(count)