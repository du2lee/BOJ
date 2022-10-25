for _ in range(3):
    a = list(map(int, input().split()))
    score = sum(a)
    if score == 0:
        print('D')
    elif score == 1:
        print('C')
    elif score == 2:
        print('B')
    elif score == 3:
        print('A')
    elif score == 4:
        print('E')