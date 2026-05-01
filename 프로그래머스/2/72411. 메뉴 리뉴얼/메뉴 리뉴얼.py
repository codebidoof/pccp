from itertools import combinations

def solution(orders, course):
    answer = []
    
    for c in course:
        myDict = {}
        for order in orders:
            order = sorted(order) # 정렬시킴 
            for comb in combinations(order, c):
                myDict[comb] = myDict.get(comb, 0) + 1
        #print(f"myDict: {myDict}")
        
        # 모든 order가 c의 길이보다 작을 경우 대비 
        if not myDict: 
            continue
        
        # 만약 가장 많이 뽑힌 조합의 개수가 2보다 작으면
        maxValue = max(myDict.values())    
        if maxValue < 2:
            continue
        
        for key, value in myDict.items():
            if value == maxValue:
                answer.append("".join(key))
        
    return sorted(answer)