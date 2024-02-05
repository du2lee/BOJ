from collections import deque

a = deque(input())
l = len(a)
for idx in range(int(input())):
    b = deque(input())

    count = 0

    while b and count < l:
        v = b.popleft()
        if v == a[count]:
            count += 1

    if count == l:
        print('#' + str(idx + 1) + ' YES')
    else:
        print('#' + str(idx + 1) + ' NO')
