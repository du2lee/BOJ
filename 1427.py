N = input()

array = [int(i) for i in N]

array.sort(reverse=True)

for i in array:
    print(i,end='')
print('')