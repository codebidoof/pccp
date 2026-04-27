from collections import deque

def solution(cards1, cards2, goal):
    que1 = deque(cards1)
    que2 = deque(cards2)
    # que3 = deque(goal)
    
    for g in goal:
        if que1 and que1[0] == g:
            que1.popleft() # dequeue
        elif que2 and que2[0] == g:
            que2.popleft() # dequeue
        else: # 둘 다의 맨 앞에 없는 순간
            return "No" # No 리턴 
    
    return "Yes" 