for idx in range(int(input())):
    answer = ""

    N, M = list(map(int, input().split()))
    S = list(input().split(" "))
    T = list(input().split(" "))

    for i in range(int(input())):
        num = int(input())
        
        n = num % N
        m = num % M

        if n == 0:
            n = N
        
        if m == 0:
            m = M

        answer = answer + S[n - 1] + T[m - 1] + " "

    print("#" + str(idx + 1) + " " + answer[:-1])