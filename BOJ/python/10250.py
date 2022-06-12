import sys

T = int(sys.stdin.readline())

for i in range(T):
    H, W, N =  map(int, sys.stdin.readline().split())
    

    Floor = N % H
    room = N // H + 1
    if Floor == 0:
        Floor = H
        room -= 1
    print(Floor * 100 + room)