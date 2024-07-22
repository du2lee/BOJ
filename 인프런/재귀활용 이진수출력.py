N = int(input())

answer = ''

def func(n, answer):
    if n == 0:
        print(answer)
        return
    answer = str(n % 2) + answer
    func(n // 2, answer)

func(N, answer)