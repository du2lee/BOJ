from collections import deque

for idx in range(int(input())):
    S = input()
    E = input()

    q = deque()
    q.append(E)

    flag = False
    reverse = False

    while q:
        s = q.popleft()

        if len(s) == len(S):
            if reverse:
                cache = ""
                for v in s:
                    cache = v + cache
                if cache == S:
                    flag = True
            else:
                if s == S:
                    flag = True
            break

        if reverse:
            if s[0] == "Y":
                reverse = False
            q.append(s[1:])
        else:
            if s[-1] == "Y":
                reverse = True
            q.append(s[:-1])

    if flag:
        print("#" + str(idx + 1) + " Yes")
    else:
        print("#" + str(idx + 1) + " No")