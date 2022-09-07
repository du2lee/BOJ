N = int(input())

array = []

def setting(array):
    return array[1]

for _ in range(N):
    name, score = input().split()
    array.append([name, int(score)])

array.sort(key=setting)

for i in array:
    print(i[0], end = ' ')
