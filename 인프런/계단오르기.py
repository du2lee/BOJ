def func(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    
    return func(N - 1) + func(N - 2)

print(func(int(input())))