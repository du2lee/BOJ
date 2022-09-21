N = int(input())

result = 665
count = 0
while True:
    result += 1
    if '666' in str(result):
        count += 1
        if count == N:
            print(result)
            break