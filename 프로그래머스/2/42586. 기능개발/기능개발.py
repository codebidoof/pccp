from collections import deque
from math import *

def availableDay(a, b): # 진행도, 속도 -> 걸리는 시간 반환
    foo = (100-a) / b
    return ceil(foo) # 올림하여 반환

def solution(progresses, speeds):
    release = []
    jobAndTerm = [] # 작업별 배포가능시점까지 걸리는 기간 저장
    
    jobAndSpeed = list(zip(progresses, speeds))
    print(jobAndSpeed)
    
    for i, r in enumerate(jobAndSpeed):
        jobAndTerm.append((i, availableDay(r[0], r[1])))
    print(f"job별 걸리는시간: {jobAndTerm}")
    
    stack = []
    current = jobAndTerm[0][1] # 현재 기준 마지막 배포일
    count = 0
        
    for i in range(len(jobAndTerm)):
        if jobAndTerm[i][1] <= current:
            count += 1 # 같이 배포
        else:
            stack.append(count)
            current = jobAndTerm[i][1]
            count = 1
            
    stack.append(count)
    return stack