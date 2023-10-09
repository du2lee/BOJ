maxValue = -10e9
minValue = 10e9

def dfs(value, signs, count):
    global maxValue
    global minValue

    if count >= N - 1:
        # 여기서 max, min 값 비교 하셈
        if maxValue < value:
            maxValue = value
        if minValue > value:
            minValue = value
    else:
        for idx in range(4):
            if signs[idx] <= 0:
                continue
            if idx == 0:
                # 덧셈
                signs[0] -= 1
                dfs(value + nums[count + 1], signs, count + 1)
                signs[0] += 1
            elif idx == 1:
                # 뺄셈
                signs[1] -= 1
                dfs(value - nums[count + 1], signs, count + 1)
                signs[1] += 1
            elif idx == 2:
                # 곱셈
                signs[2] -= 1
                dfs(value * nums[count + 1], signs, count + 1)
                signs[2] += 1
            elif idx == 3:
                # 나눗셈
                signs[3] -= 1
                cache = 0
                if (value < 0 and nums[count + 1] > 0) or (value > 0 and nums[count + 1] < 0):
                    cache -= abs(value) // abs(nums[count + 1])
                else:
                    cache += value // nums[count + 1]
                dfs(cache, signs, count + 1)
                signs[3] += 1

N = int(input())
nums = list(map(int, input().split()))
signs = list(map(int, input().split()))

dfs(nums[0], signs, 0)

print(maxValue)
print(minValue)