def solution(arr):
    answer = [arr[0]]
    
    for idx in range(1, len(arr)):
        if arr[idx] == arr[idx - 1]:
            continue
        answer.append(arr[idx])

    return answer