while True:

    try:
        N = input()
        lower = upper = num = blank = 0
        for idx in N:
            if 97 <= ord(idx) and ord(idx) <= 122:
                lower += 1
            elif 65 <= ord(idx) and ord(idx) <= 90:
                upper += 1
            elif 48 <= ord(idx) and ord(idx) <= 57:
                num += 1
            elif idx == ' ':
                blank += 1
        print(lower, upper, num, blank)
    except EOFError :
        break