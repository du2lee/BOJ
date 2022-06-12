# N = int(input())
# num = 2 * N - 1

# for idx in range(1, N + 1):
#     num2 = 2 * idx - 1
#     string = "{0:^" + str(num) + "}"
#     print(string.format('*'* num2))

N = int(input())

for idx in range(1, N + 1):
    print(' ' * (N - idx) + '*' * idx + '*' * (idx - 1))

