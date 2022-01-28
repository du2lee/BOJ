if __name__ == '__main__':
    s = input()
    flag_num = False
    flag_alpha = False
    flag_digit = False
    flag_lower = False
    flag_upper = False
    for idx in s:
        if idx.isalnum():
            flag_num = True
        if idx.isalpha():
            flag_alpha = True
        if idx.isdigit():
            flag_digit = True
        if idx.islower():
            flag_lower = True
        if idx.isupper():
            flag_upper = True
        
        if flag_num and flag_alpha and flag_digit and flag_lower and flag_upper:
            break     
            
    print(flag_num)
    print(flag_alpha)
    print(flag_digit)
    print(flag_lower)
    print(flag_upper)