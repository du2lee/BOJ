while True:
    cache = input()
    if cache == '0':
        break
    cache2 = ''
    for i in cache:
        cache2 = i + cache2
    
    if cache == cache2:
        print('yes')
    else:
        print('no')
    