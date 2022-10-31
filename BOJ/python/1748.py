N = int(input())
length = len(str(N))

answer = 0

if length == 1:
    answer = N
else:
    answer = 9
    for i in range(2 , length):
        answer += i * ((10 ** i) -(10 ** (i - 1)))
    answer +=  length * ((N - (10 ** (length - 1))) + 1)

print(answer)