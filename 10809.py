input_Str = input()
list_alphabet = [-1 for i in range(26)]
for j in range(len(input_Str)):
    if list_alphabet[ord(input_Str[j]) - 97] == -1:
        list_alphabet[ord(input_Str[j]) - 97] = j
for k in range(26):
    print(list_alphabet[k],end=" ")