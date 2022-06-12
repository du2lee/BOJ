a, b = map(int, input().split())
days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
if a == 2 or a == 3 or a == 11:
    b += 3
elif a == 4 or a == 7:
    b += 6
elif a == 5:
    b += 1
elif a == 6:
    b += 4
elif a == 8:
    b += 2
elif a == 9 or a == 12:
    b += 5

print(days[b%7])

