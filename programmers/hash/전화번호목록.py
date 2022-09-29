def solution(phone_book):
    answer = True
    phone_book.sort()
    flag = False
    N = len(phone_book)
    
    for i in range(N - 1):
        lenI = len(phone_book[i])
        for j in range(i + 1, N):
            lenJ = len(phone_book[j])
            if lenI > lenJ:
                continue
            # 시간복잡도를 줄여주는 Key Point -> ["123", "1000", "123404595"]이라는 array가 있을 때 array.sort()는 ["123", "123404595", "1000"]을 활용 
            if phone_book[i][0] != phone_book[j][0] or phone_book[i][lenI -1] != phone_book[j][lenI -1]:
                break
            
            if phone_book[i] == phone_book[j][:lenI]:
                flag = True
                answer = False
                break
        if flag:
            break

    return answer









# 시간 초과 코드 (91.7점)
# def solution(phone_book):
#     answer = True
#     phone_book.sort()
#     flag = False
#     N = len(phone_book)
    
#     for i in range(N - 1):
#         lenI = len(phone_book[i])
#         for j in range(i + 1, N):
#             lenJ = len(phone_book[j])
#             if lenI > lenJ:
#                 continue
            
#             if phone_book[i] == phone_book[j][:lenI]:
#                 flag = True
#                 answer = False
#                 break
#         if flag:
#             break

#     return answer