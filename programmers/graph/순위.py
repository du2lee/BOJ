def solution(n, results):
    answer = 0
    winners = [set() for _ in range(n + 1)]
    losers = [set() for _ in range(n + 1)]

    for win, lose in results:
        losers[win].add(lose)
        winners[lose].add(win)
         
    for i in range(1, n + 1):
        for j in winners[i]:
            losers[j].update(losers[i])
        for j in losers[i]:
            winners[j].update(winners[i])
    
    for i in range(1, n + 1):
        if len(winners[i]) + len(losers[i]) == n - 1:
            answer += 1
    
    return answer