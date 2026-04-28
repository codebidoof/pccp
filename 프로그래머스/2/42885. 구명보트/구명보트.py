from collections import deque

def solution(people, limit):
    count = 0
    people = deque(sorted(people, reverse = True)) # 내림차순 정렬 후 deque로
    
    while people:
        heavy = people.popleft()
        if people and heavy + people[-1] <= limit: # 무거운사람 + 가벼운사람 <= limit
            people.pop() # 같이 태움
        count += 1
    
    return count