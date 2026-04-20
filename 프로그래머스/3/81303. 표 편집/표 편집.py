def solution(n, k, cmd):
    stack = [] # 삭제된 entity를 담는 스택
    current = k #선택상태인 행 번호. 고유 행 번호를 포인터가 가리키는 메모리 주소로 생각하자.
    cmdList = [] # 명령어들 리스트
    
    # [left, 고유 행 번호, right]
    entityList = [[i-1, i, i+1 if i < n-1 else -1] for i in range(n)] 
        
    # 입력 명령어들 파싱해서 저장
    for c in cmd:
        if " " in c:
            cmdList.append(c.split(" "))
        else:
            cmdList.append(c)
            
    # 명령어 순차적으로 실행        
    for cm in cmdList:
        if cm[0] == "U":
            for _ in range(int(cm[1])) :
                current = entityList[current][0] # left필드를 통해 갱신
        elif cm[0] == "D": 
            for _ in range(int(cm[1])):
                current = entityList[current][2] # right필드를 통해 갱신
        elif cm == "C": # 삭제
            temp = entityList[current] # 삭제할 노드
            l = temp[0] # 삭제할 노드의 이전 거
            r = temp[2] # 삭제할 노드의 다음 거
            
            # 왼쪽 연결 처리
            if l != -1: 
                entityList[l][2] = r
            # 오른쪽 연결 처리
            if r != -1: 
                entityList[r][0] = l
                
            stack.append(temp[:])
            current = r if r != -1 else l
            
        elif cm == "Z": # 복원
            temp = stack.pop()
            l = temp[0] 
            v = temp[1]
            r = temp[2]
            
            if l != -1:
                entityList[l][2] = v
            if r != -1:
                entityList[r][0] = v
                
    anslist = ["O"]*n            
    while stack:
        temp = stack.pop()
        anslist[temp[1]] = "X"
    
    answer = "".join(anslist)
    return answer