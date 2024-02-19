from collections import deque

for idx in range(int(input())):
    flag = True
    string = deque(input())

    while len(string) > 1:
        front = string.popleft()
        back = string.pop()

        if front.lower() != back.lower():
            flag = False

    if flag:
        print('#' + str(idx + 1) + ' YES')
    else:
        print('#' + str(idx + 1) + ' NO')