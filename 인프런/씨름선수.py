people = []
N = int(input())
for _ in range(N):
    people.append(list(map(int, input().split())))

people.sort(reverse=True)

answer = 1
maxKg = people[0][1]

for idx in range(1, N):
    if maxKg < people[idx][1]:
        answer += 1
        maxKg = people[idx][1]

# 완전 탐색
# answer = 0
# people.sort()
# for idx in range(N):
#     for cm, kg in people:
#         if cm > people[idx][0] and kg > people[idx][1]:
#             flag = False
#             break
#     else:
#         answer += 1

print(answer)