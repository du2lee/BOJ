H, M = map(int, input().split())
if H == 0 and M < 45:
    print("23", M+15)
elif M < 45:
    print(H-1, M+15)
else:
    print(H, M-45)