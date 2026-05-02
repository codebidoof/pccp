import math

def solution(progresses ,speed):
    answer = []
    n = len(progresses)

    # 각 작업의 배포 가능일을 계산
    days_left = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(n)]

    count = 0 # 배포될 작업의 수 카운트
    max_day = days_left[0] # 현재 배포될 작업 중 가장 늦게 배포될 작업의 가능일

    for i in range(n):
        if days_left[i] <= max_day: # 배포 가능일이 가장 늦은 배포일보다 빠르면
            count += 1
        else: # 배포 예정일이 기준 배포일보다 느리면,
            answer.append(count)
            count = 1
            max_day = days_left[i]

    answer.append(count) # 마지막으로 카운트된 작업을 함께 배포
    return answer

import heapq

def solution(people, limit):
    n = len(people)
    count = 0    
    boat = 0 # 현재 보트에 탄 무게
    people.sort() # 오름차순 정렬
    
    for p in people:
        if boat + p < limit:
            boat += p
        elif boat + p == limit:
            count += 1
            boat = 0
        else:
            count += 1
            boat = 0
            boat += p
    
    if boat > 0:
        count += 1
        
    return count