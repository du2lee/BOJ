def d():
    list_self = [0 for i in range(10001)]
    list_self[0] = 1
    cache = 0
    for i in range(1,10001):
        if i < 10:
            cache = i+i
        elif i <= 100:
            cache = i+(i//10)+(i%10)
        elif i <=1000:
            cache = i+(i//100)+((i//10)%10)+(i%10)
        elif i <=10000:
            cache = i+(i%10)+((i//10)%10) + ((i//100)%10) + (i//1000)
        if cache <= 10000:
            list_self[cache] = 1

    for j in range(10000):
        if list_self[j] == 0:
            print(j)

d()