for i in range(int(input())):

    A, B, C = list(map(int, input().split()))
    
    answer = 0

    if C < 2 or B < 1:
        answer = -1
    else:
        if C <= B:
            eat = (B - C + 1)
            answer += eat
            B -= eat

        if B <= A:
            eat = (A - B + 1)
            answer += (A - B + 1)
            A -= eat

    if A == 0:
        answer = -1

    print("#" + str(i + 1) + " " + str(answer))