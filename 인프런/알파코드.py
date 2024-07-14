codes = input()

answer = []
count = 0

def dfs(idx, flag):

    global count
    if idx >= len(codes):
        if ''.join(answer) == codes:
            count += 1
            for v in answer:
                print(chr(64 + int(v)), end="")
            print()
        return
    
    code = codes[idx]

    # 앞의 숫자 관여
    if flag == '1':
        answer.append(flag + code)
        dfs(idx + 1, '0')
        answer.pop()

    elif flag == '2':
        answer.append(flag + code)
        dfs(idx + 1, '0')
        answer.pop()

    # 앞의 숫자 관여 X
    else:
        if code == '0':
            return

        if code != '1' and code != '2':
            answer.append(code)
            dfs(idx + 1, '0')
            answer.pop()
        else:
            answer.append(code)
            dfs(idx + 1, '0')
            answer.pop()

            dfs(idx + 1, code)

dfs(0, '0')

print(count)