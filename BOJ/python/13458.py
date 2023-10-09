# import sys

# N = int(sys.stdin.readline())
# people = list(i for i in map(int, sys.stdin.readline().split()))
# B, C = map(int, sys.stdin.readline().split())
# sum = 0

# for i in range(N):
#     if people[i] <= B:
#         sum += 1
#     else:
#         cache = (people[i] - B) % C
#         assistant = int((people[i] - B) / C)
#         if cache == 0:
#             sum += assistant + 1
#         else:
#             sum += assistant + 2

# print(sum)





N = int(input())
A = list(map(int, input().split()))
B, C = list(map(int, input().split()))

answer = N

for idx in range(N):
    people = A[idx] - B
    if people < 0:
        continue
    elif people % C == 0:
        answer += people // C
    elif people > 0:
        answer += people // C + 1

print(answer)    