num, m = list(map(int, input().split()))

s = list(str(num))
ans = []

for idx in range(len(s)):

    while True:
        if len(ans) == 0 or m == 0:
            ans.append(s[idx])
            break

        if ans[-1] < s[idx]:
            ans.pop()
            m -= 1
        else:
            ans.append(s[idx])
            break

ans = ans[:len(ans) - m]
print(''.join(ans))

