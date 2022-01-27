def swap_case(s):
    array = []
    for idx in s:
        cache = ord(idx)
        if 65 <= cache and cache <= 90:
            cache +=32
        elif 97 <= cache and cache <= 122:
            cache -=32
        array.append(chr(cache))
        result = "".join(array)
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)