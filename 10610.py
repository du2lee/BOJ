# if __name__ == "__main__":
#     N = list(input())
#     N.sort(reverse = True)
#     sum = 0
#     for i in N:
#         sum += int(i)
#     if sum % 3 != 0 or '0' not in N:
#         print(-1)
#     else:
#         print("".join(N))


N = int(input())

array = []

while N >= 10:
    array.append(N % 10)
    N = int(N / 10)
array.append(N)

array.sort(reverse=True)

a = array.pop()
sumArray = sum(array)

if a != 0 or sumArray % 3 != 0:
    print(-1)
    exit()

for i in array:
    print(i, end='')
print(a)