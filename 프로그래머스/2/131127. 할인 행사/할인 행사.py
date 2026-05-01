from collections import deque
import copy

def solution(want, number, discount):
    term = sum(number) # 기간
    myList = list(zip(want, number))
    print(f"myList: {myList}")
    
    myDict = {}
    for m in myList:
        myDict[m[0]] = m[1]
    #print(f"myDict: {myDict}")
    
    answer = 0
    start = 0
    while start + term - 1 <= len(discount) - 1:
        newDict = copy.deepcopy(myDict) # 딕셔너리 깊은 복사
        #print(f"newDict: {newDict}")

        # 시작점부터 term의 기간동안
        for i in range(start, start + term):
            currentGood = discount[i] # 현재 상품
            if currentGood in newDict.keys() and newDict[currentGood] > 0: 
                newDict[currentGood] -= 1
        
        #print(f"newDict: {newDict}")
        if all(v == 0 for v in newDict.values()): # 다 살수 있으면
            answer += 1
        
        start += 1
    
    return answer