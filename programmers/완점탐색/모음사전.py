moum = ' AEIOU'

dictionary = []

def dfs(words, n):
    if n == 0:
        dictionary.append(words.replace(' ', ''))
        return
    
    for a in moum:
        if a != ' ' and n < len(moum) - 1:
                if words[-1] == ' ':
                    return    
        dfs(words + a, n - 1)


def solution(word):
    global dictionary
    answer = 0
    
    dfs('', len(moum) - 1)
    dictionary = dictionary[1:]
    for idx in range(len(dictionary)):
        if word == dictionary[idx]:
            answer = idx + 1
            break
            
    return answer