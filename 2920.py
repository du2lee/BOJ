import sys

# input_Array = list(map(int, sys.stdin.readline().split()))                        //첫번째 방법

# if input_Array[0] == 1:
#     for i in range(0, len(input_Array)):
#         if input_Array[i] != i + 1:
#             print("mixed")
#             exit()
#     print('ascending')
# elif input_Array[0] == 8:
#     for i in range(0, len(input_Array)):
#         if input_Array[i] != 8 - i:
#             print("mixed")
#             exit()
#     print('descending')
# else:
#     print("mixed")


array = list(map(int, sys.stdin.readline().split()))

ascending = True
descending = True

for i in range(1,len(array)):
    if array[i] > array[i - 1]:
        descending = False
    elif array[i] < array[i -1]:
        ascending = False

if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print("mixed")