for idx in range(int(input())):
    s = input()
    bell = int(s[4:]) % 2

    answer = "1"
    if(s[0] == "o" and bell == 0):
        answer = "0"

    if(s[1] == "o" and bell == 1):
        answer = "0"

    if s[2] == "o":
        if int(s[4:]) == 0:
            answer = "2"
        elif bell == 0:
            answer = "0"

    print("#" + str(idx + 1)  + " " + answer)