X = int(input())

def func(X):
    count = 0
    while X >= 1:
        cache = X % 2
        X //= 2
        if cache == 1:
            count += 1
    print(count)

func(X)