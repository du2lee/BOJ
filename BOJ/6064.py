import sys


if __name__ == "__main__":
    T = int(sys.stdin.readline())

    for _ in range(T):
        M, N, x, y = map(int, sys.stdin.readline().split())
        flag = True
        while x <= M * N:
            if x % N == y % N:
                print(x)
                flag = False
                break
            x += M
        if flag:
            print(-1)
            
            

            '''if count > M * N:                    // 시간초과코드
                print(-1)
                break
            if count_x == x and count_y == y:
                print(count)
                break
            if count_x == M and count_y == N:
                count_x = 1
                count_y = 1
            elif count_x == M:
                    count_x = 1
                    count_y += 1
            elif count_y == N:
                count_y = 1
                count_x += 1
            else:
                count_x += 1
                count_y += 1
            count += 1'''