N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
robots = [False] * N * 2

answer = 0

while True:
    answer += 1

    # 벨트 움직이기
    A = [A[-1]] + A[: -1]
    robots = [robots[-1]] + robots[: -1]
    robots[N - 1] = False   # 로봇 내리기
    
    # 로봇 이동하기
    for idx in range(N - 2, -1, -1):
        if not(robots[idx]):
            continue

        if(A[idx + 1] > 0 and not(robots[idx + 1])):
            robots[idx + 1] = True
            robots[idx] = False
            A[idx + 1] -= 1

    robots[N - 1] = False   # 로봇 내리기

    # 로봇 올리기
    if (A[0] > 0 and not(robots[0])):
        robots[0] = True
        A[0] -= 1

    # 내구도 0 일 경우 카운트 올리기
    count = 0
    for value in A:
        if value <= 0:
            count += 1

    if count >= K:
        break

print(answer)