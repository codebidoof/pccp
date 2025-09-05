#내 풀이 - 왜 런타임 에러가 나는지 모르겠음..
from collections import deque

def solution(cards1, cards2, goal):
    temp = 0 # 골을 순회할 포인터 역할
    result = [] #골과 최종결과를 비교할 리스트
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    while len(cards1) > 0 and len(cards2) > 0: 
        if cards1[0] == goal[temp]:
            result.append(cards1.popleft())
        elif cards2[0] == goal[temp]:
            result.append(cards2.popleft())
        temp += 1
        
    if not cards1: #1번 덱이 공백일 때
        result += list(cards2)
    else: #2번 덱이 공백일 경우
        result += list(cards1)
        
    return "Yes" if result == goal else "No"

# 책 풀이 - 비교군과 비교하지 말고 골까지 큐로 관리한다.
def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)

    #골의 문자열을 순차적으로 순회
    while goal:
        if cards1 and cards1[0]==goal[0]:
            cards1.popleft()
            goal.popleft()
        elif cards2 and cards2[0]==goal[0]:
            cards2.popleft()
            goal.popleft()
        else:
            break #일치하는 원소를 찾지 못했으므로 종료
    
    return "Yes" if not goal else "No"
    
