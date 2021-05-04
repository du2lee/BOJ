import sys
input_Str = sys.stdin.readline()
sum = 0

for j in range(len(input_Str) - 1):
    if input_Str[j] >= chr(65) and input_Str[j] <= chr(67):
        sum += 3
    elif input_Str[j] >= chr(68) and input_Str[j] <= chr(70):
        sum += 4
    elif input_Str[j] >= chr(71) and input_Str[j] <= chr(73):
        sum += 5
    elif input_Str[j] >= chr(74) and input_Str[j] <= chr(76):
        sum += 6
    elif input_Str[j] >= chr(77) and input_Str[j] <= chr(79):
        sum += 7
    elif input_Str[j] >= chr(80) and input_Str[j] <= chr(83):
        sum += 8
    elif input_Str[j] >= chr(84) and input_Str[j] <= chr(86):
        sum += 9
    elif input_Str[j] >= chr(87) and input_Str[j] <= chr(90):
        sum += 10
print(sum)