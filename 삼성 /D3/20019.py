for idx in range(int(input())):
    answer = "YES"

    string = input()
    half = len(string) // 2

    for i in range(half):
        if string[i] != string[half + i + 1]:
            answer = "NO"
            break

    print("#" + str(idx + 1) + " " + answer)