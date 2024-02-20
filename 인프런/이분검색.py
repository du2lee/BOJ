N, M = list(map(int, input().split()))
nums = list(map(int, input().split()))
nums.sort()

def func(s, e):
    if s > e:
        return

    mid = (s + e) // 2

    if(nums[mid] == M):
        print(mid + 1)
    elif(nums[mid] > M):
        func(s, mid - 1)
    else:
        func(mid + 1, e)

func(0, N - 1)

# # 시간초과 코드
# for idx in range(N):
#     if nums[idx] == M:
#         print(idx + 1)
#         break
# else:
#     print(-1)