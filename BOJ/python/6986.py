N, K = map(int, input().split())

score = []
for _ in range(N):
    score.append(float(input())*10)

score = sorted(score)[K:N-K]

jp=0
for i in score:
    jp+=i
jp = jp/(N-2*K)/10
#jp = round(jp, 2)


bp=0
for i in score:
    bp+=i
bp = bp + score[0]*K + score[-1]*K
bp = bp/N/10
#bp = round(bp, 2)

print("{:.2f}\n{:.2f}".format(jp + 0.00000001, bp + 0.00000001))