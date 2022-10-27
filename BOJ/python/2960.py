# import sys

# count = 0

# if __name__ == "__main__":
#     N, K = map(int, sys.stdin.readline().split())
#     flags = [False, False] + [True] * (N - 1)
#     for i in range(2, N + 1):
#         if flags[i]:
#             count += 1
#             if count == K:
#                 print(i)
#                 exit()
#             for j in range(2 * i, N + 1, i):
#                 if flags[j] == False:
#                     continue
#                 flags[j] = False
#                 count += 1
#                 if count == K:
#                     print(j)
#                     exit()

N , K = list(map(int, input().split()))
flags = [True, True] + [False for _ in range(N - 1)]
count = 0

for i in range(2, N + 1):
    if not flags[i]:
        flag = False
        count += 1
        flags[i] = True
        if count == K:
            print(i)
            break
        
        for j in range(i * 2, N + 1, i):
            if not flags[j]:
                count += 1
                flags[j] = True
                if count == K:
                    print(j)
                    flag = True
                    break
        if flag:
            break