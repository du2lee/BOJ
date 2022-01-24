import sys

input_Str = sys.stdin.readline()
sum = 0
i = 0
while i < (len(input_Str) - 1):
    if input_Str[i] == 'd' and input_Str[i+1] == 'z' and input_Str[i+2] == '=':
        sum += 1
        i += 2
    elif input_Str[i] =='c' and (input_Str[i + 1] == '=' or input_Str[i + 1] == '-'):
        sum +=1
        i += 1
    elif input_Str[i + 1] == '=':
        sum +=1
        i += 1
    elif input_Str[i] == 'd' and input_Str[i+1] == '-':
        sum += 1
        i += 1
    elif input_Str[i] == 'l' and input_Str[i+1] == 'j':
        sum += 1
        i += 1
    elif input_Str[i] == 'n' and input_Str[i+1] == 'j':
        sum += 1
        i += 1
    else:
        sum += 1
    i += 1
    

print(sum)