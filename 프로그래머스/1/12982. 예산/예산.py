import heapq

def solution(d, budget):
    count = 0
    
    heapq.heapify(d) # d를 힙큐로 바꿈
    
    while d and d[0] <= budget:
        budget -= heapq.heappop(d)
        count += 1
    
    return count