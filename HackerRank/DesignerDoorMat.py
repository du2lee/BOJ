h, w = map(int,input().split())

design = '.|.'
half = h // 2

def odd(num):
    return 2 * num - 1

def bottom(num):
    return 2 * half - num + 2

for idx in range(1, h + 1):
    if idx == half + 1:
        print('WELCOME'.center(w, '-'))
    elif idx < half + 1:
        print((design * odd(idx)).center(w, '-'))
    else:
        print((design * odd(bottom(idx))).center(w, '-'))