import sys

L, C = map(int, sys.stdin.readline().split())

str = list(i for i in input().split())

str.sort()
vowel = list()
consonant = list()
array = list()

for i in str:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vowel.append(i)
    else:
        consonant.append(i)

def func(N):
    if len(array) == L:
        count_v = 0
        count_c = 0
        
        for j in array:
            if j in vowel:
                count_v += 1
            if j in consonant:
                count_c += 1
            if count_v >= 1 and count_c >= 2:
                for k in array:
                    print(k,end='')
                print('')
                break
        return
    
    for i in range(N ,len(str)):
        array.append(str[i])
        func(i + 1)
        array.pop()
func(0)