# 내 풀이 - 틀림 ㅠㅠ 원인: 스택의 top이 작업 그룹의 최대 걸리는 일수를 보장하지 않음
from collections import deque
import math

def solution(progresses, speeds):
    que = deque()
    stack = []
    answer = []
    for i in range(len(progresses)):
        days = math.ceil((100-progresses[i])/speeds[i])
        que.append(days) # [7, 2, 9]
    while que : # 큐가 빌 때까지
        stack.append(que.popleft())
        if que and que[0] > stack[-1]: # 큐가 공백이 아닐 조건 추가
            answer.append(len(stack))
            stack.clear()

    if len(stack) > 0:
        answer.append(len(stack)) #마지막에 스택에 남은거 처리
    return answer

#책 풀이 - 배포 예정일을 미리 구했다가 배포일이 되었을 때 몇개의 작업이 완료되었는지 체크
import math
def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    days_left = [math.ceil((100-progresses[i]) / speeds[i]) for i in range(n)]

    count = 0 # 배포될 작업의 수 카운트
    max_day = days_left[0] # 현재 배포될 작업 중 가장 늦게 배포될 작업의 가능일
    for i in range(n):
        if days_left[i] <= max_day: # 베포 가능일이 기준 배포일보다 느리면
            count += 1
        else:  #배포 예정일이 기준 배포일보다 느리면
            answer.append(count) #이전 그룹 배포 완료!
            count = 1 # 카운트 다시 초기화
            max_day = days_left[i] #기준 변경 
        answer.append(count) # 마지막으로 카운트된 작업들을 함께 배포
        return answer # 테스트

#비교용
