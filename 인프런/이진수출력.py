answer = ''

def func(N):
    global answer
    if N == 0:
        return
    value = N // 2
    mod = N % 2

    answer = str(mod) + answer
    func(value)

func(int(input()))
print(answer)