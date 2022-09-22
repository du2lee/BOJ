numA, numB = list(map(int, input().split()))

A = list(map(int, input().split()))
B = list(map(int, input().split()))

a_b = set(A)
b_a = set(B)

for i in B:
    try:
        a_b.remove(i)
    except:
        pass

for i in A:
    try:
        b_a.remove(i)
    except:
        pass

print(len(a_b)+len(b_a))

