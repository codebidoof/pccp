def solution(record):
    userDict = {} # id, 닉
    tpDict = {
        "Enter": "들어왔습니다.", 
        "Leave": "나갔습니다.", 
    }
    result = []
    
    newRecord = []
    for r in record: #O(n) 
        temp = r.split(" ")
        
        if temp[0] == "Enter":
            if not temp[1] in userDict: # 처음 보는 id면
                userDict[temp[1]] = userDict.get(temp[1], "") + temp[2] # userDict에 삽입
            elif temp[2] != userDict[temp[1]]: # 닉이 달라졌다면
                userDict[temp[1]] = temp[2] # 닉 갱신
                
        elif temp[0] == "Change":
            userDict[temp[1]] = temp[2] # id갱신
            
        else: # 리브
            pass
            #userDict[temp[1]] = ""
        
        tmp = temp[:2] # 닉은 갖다버림 -> 추후 딕셔너리로 매칭
        newRecord.append(tmp)
    #print(f"newRecord: {newRecord}")
    #print(f"userDict: {userDict}")
    
    result = []
    for nr in newRecord:
        if nr[0] == "Change":
            continue
        else:
            result.append(f"{userDict[nr[1]]}님이 {tpDict[nr[0]]}")
    
    return result