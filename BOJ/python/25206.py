grades = {}
grades['A+'] = 4.5
grades['A0'] = 4.0
grades['B+'] = 3.5
grades['B0'] = 3.0
grades['C+'] = 2.5
grades['C0'] = 2.0
grades['D+'] = 1.5
grades['D0'] = 1.0
grades['F'] = 0.0

counts = 0
scores = 0

for _ in range(20):
    name, count, grade = input().split()
    if grade == 'P':
        continue
    counts += float(count)
    scores += float(count) * float(grades[grade])

print('{0:.6f}'.format(round(scores / counts, 6)))