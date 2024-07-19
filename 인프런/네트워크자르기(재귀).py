N = int(input())

def func(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    return func(n - 1) + func(n - 2)

print(func(N))

# def func(n):
#     if n == 1:
#         return 1
    
#     if n == 2:
#         return 2
    
#     return func(n - 1) + func(n - 2)

# print(func(N))