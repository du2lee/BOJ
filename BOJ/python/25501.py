T = int(input())


def isPalindrome(s, start, end):
    global count

    if start >= end:
        count += 1
        return 1
    
    if s[start] != s[end]:
        count += 1
        return 0
    else:
        count += 1
        return isPalindrome(s, start + 1, end - 1)


for _ in range(T):
    string = input()
    count = 0
    result = isPalindrome(string, 0, len(string) - 1)
    print(result, count)