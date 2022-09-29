def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    for idx in range(len(completion)):
        if participant[idx] != completion[idx]:
            answer = participant[idx]
            break
    if answer == '':
        answer = participant[-1]
    
    return answer