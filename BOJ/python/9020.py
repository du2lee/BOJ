import sys, math

T = int(sys.stdin.readline())

def listPrimes(N):
    list_prime = []
    for i in range(1, N):
        a =False
        if i == 1:
            pass
        else:
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    a = True
                    break
            if a == False:
                list_prime.append(i)
    return list_prime


def sumlist(list_prime):
    idx = max([i for i in range(len(list_prime)) if list_prime[i] <= N / 2])

    for i in range(idx, -1, -1):
        for j in range(idx, len(list_prime)):
            if list_prime[i] + list_prime[j] == N:
                return list_prime[i], list_prime[j]

for k in range(T):
    N = int(sys.stdin.readline())
    
    list_prime = listPrimes(N)
    a, b = sumlist(list_prime)
    
    
    print(a, b)
    
    





#def isPrime(value):
#    if value == 1:
#        return False
#    for i in range(2, int(math.sqrt(value))+1):
#        if value % i == 0:
#            return False
#    return True

#def sumPrimes(N):
#    a = 0
#    b = 10000
#     for i in range(2, int(N / 2) + 1):
#        if isPrime(i):
#            for j in range(i, N):
#                if isPrime(j) and i + j == N:
#                    if b - a > j - i:
#                        a, b = i, j
#    print(a, b)



#---------------------------------------------


#for i in range(T):
#    N = int(sys.stdin.readline())
#    sumPrimes(N)



# i = 0
#while list_prime[i] < int(N / 2) + 1:
#    for j in range(i , len(list_prime)):
#        if list_prime[i] + list_prime[j] == N:
#                if b - a > list_prime[j] - list_prime[i]:
#                    a, b = list_prime[i], list_prime[j]
#                    break
#    i += 1