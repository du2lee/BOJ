N, L = list(map(int, input().split()))

maps = [list(map(int, input().split())) for _ in range(N)]

answer = 0

def func(maps):
    global answer
    for idx in range(N):
        flag = True
        check = [True for _ in range(N)]

        for j in range(1, N):
            pre = maps[idx][j - 1]
            now = maps[idx][j]
            compare = abs(pre - now)

            if compare > 1: # 1 이상 차이가 날 경우
                flag = False
                break
            elif compare == 0: # 같음:
                continue
            elif compare == 1: # 1일 경우
                if pre > now:
                    # out of range 검사
                    if j + L > N:
                        flag = False
                        break  
                    cache = maps[idx][j]
                    # 처리
                    for k in range(j, j + L): 
                        if cache != maps[idx][k]: # 낮은부분 연속에서 같은지 검사
                            flag = False
                            break
                        if not check[k]:    # 중복 경사
                            flag = False
                            break
                        check[k] = False
                else:
                    # out of range 검사
                    if j - L - 1 < -1:
                        flag = False
                        break  
                    cache = maps[idx][j - 1]
                    # 처리
                    for k in range(j - 1, j - L - 1, -1): 
                        if cache != maps[idx][k]: # 낮은부분 연속에서 같은지 검사
                            flag = False
                            break
                        if not check[k]:    # 중복 경사
                            flag = False
                            break
                        check[k] = False      
                if not flag:
                    break
        if flag:
            answer += 1
# 가로줄
func(maps)

# 세로줄
maps2 = []
for i in zip(*maps):
    maps2.append(list(i))
func(maps2)

# answer
print(answer)