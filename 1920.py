# N = int(input())
# A = list(map(int,input().split()))
# M = int(input())
# B = list(map(int,input().split()))

# for idx in B:                                 //시간초과 코드
#     flag = False
#     for idx2 in A:
#         if idx == idx2:
#             flag = True
#             break
#     if flag:
#         print(1)
#     else:
#         print(0)


# array = [0] * 2147483649                   //메모리초과 코드

# for idx in A:
#     array[idx] += 1

# for idx in B:
#     if array[idx] == 1:
#         print(1)
#     else:
#         print(0)


N = int(input())
A = set(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))
