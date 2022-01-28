# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())
array = set()

for i in range(T):
    count_alphabet = 0
    count_num = 0
    flag = True
    cache = input()
    if len(cache) != 10:
        print('Invalid')
        continue

    for idx in cache:
        if ord(idx) >= 48 and ord(idx) <= 57:
            count_num += 1
        elif ord(idx) >= 65 and ord(idx) <= 90:
            count_alphabet += 1
        elif ord(idx) >= 97 and ord(idx) <= 122:
            count_alphabet += 1
        else:
            flag = False

    if count_alphabet >= 2 and count_num and flag:
        if cache not in array:
            if len(array) == 0:
                print('Invalid')
                array.add(cache)
            else:
                print('Valid')
                array.add(cache)
    else:
        print('InValid')