def solution(nums):
    answer = 0
    dogam = set()
    half = len(nums) // 2
    for i in nums:
        dogam.add(i)
    
    dagamLength = len(dogam)
    
    if half > dagamLength:
        answer = dagamLength
    else:
        answer = half
    
    return answer