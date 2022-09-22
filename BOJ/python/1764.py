N, M = list(map(int, input().split()))

noHear = dict()
result= []

for i in range(N):
    a = input()
    noHear[a] = a

for i in range(M):
    try:
        result.append(noHear[input()])
    except:
        pass
    
print(len(result))
result.sort()
for i in result:
    print(i)