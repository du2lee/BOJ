while(True):
    first, second = list(map(int, input().split()))
    if first == 0 and second == 0:
        break
    elif first > second:
        print("Yes")
    else:
        print("No")