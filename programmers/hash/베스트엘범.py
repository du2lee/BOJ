def solution(genres, plays):
    answer = []
    albam = dict()
    count = dict()
    arr = []
    for genre in genres:
        albam[genre] = []
        count[genre] = 0
    
    for idx in range(len(genres)):
        albam[genres[idx]].append((plays[idx], idx))
        count[genres[idx]] += plays[idx]
        
    for k in count:
        arr.append((count[k], k))
        
    arr.sort(reverse=True)
        
    for genre in genres:
        albam[genre].sort(key = lambda x : (-x[0], x[1]))
        
    for summary, type in arr:
        addIdx = 0
        for views, idx in albam[type]:
            if addIdx >= 2:
                break
            answer.append(idx)
            addIdx += 1
    
    return answer