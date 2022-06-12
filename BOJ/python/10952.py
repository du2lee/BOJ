# while True:
#     a, b = map(int, input().split())
#     if(a==0 and b==0):
#         break
#     print(a+b)

while True:
    a, b = input().split()
    if a == '0' and b == '0':
        break
    a = int(a)
    b = int(b)
    print(a+b)