N = int(input())

if N == 1:
    print(input())

else:
    first = input()
    length = len(first)
    answer = []
    for i in first:
        answer.append(i)
    for _ in range(N - 1):
        command = input()

        for i in range(length):
            if answer[i] != command[i]:
                answer[i] = '?'
    print(''.join(answer))