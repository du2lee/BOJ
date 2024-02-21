from collections import deque

N = int(input())
arr = deque(map(int, input().split()))

check = 0
left = 0
right = N - 1
while left <= right:
    cache = [(arr[left], 'L'), (arr[right], 'R')]
    cache.sort()

    for v, s in cache:
        if check < v:
            check = v
            print(s, end="")
            if s == 'L':
                left += 1
            else:
                right -= 1
            break
    else:
        break


    