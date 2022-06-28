N = input()

for idx in N:
    idx = ord(idx)
    if 65 <= idx and idx < 91:
        if idx < 78:
            idx += 13
        else:
            idx -= 13
    elif 97 <= idx and idx < 123:
        if idx < 110:
            idx += 13
        else:
            idx -= 13
    print(chr(idx), end="")