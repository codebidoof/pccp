def solution(board, moves):
    n = len(board)
    
    wheres = [m-1 for m in moves] # [0, 4, 2, 4, 0, 1, 0, 3]
    
    newBoard = [[] for _ in range(n)] # n행짜리 이차원 배열 생성. 각 행은 빈 상태
    
    for i in range(n-1, -1, -1): # 역순탐색, 0 까지..!
        for j in range(n):
            if board[i][j]==0:
                continue
            newBoard[j].append(board[i][j])
    print(newBoard)
    basket = [] # 바구니
    count = 0
    
    for w in wheres:
        doll = -1
        if newBoard[w]: # 해당하는 보드가 안비어있다면
            doll = newBoard[w].pop() # 팝
        if basket and doll == basket[-1]: # 바구니 top과 꺼낸 인형이 같다면
            basket.pop()
            count += 2
        elif doll != -1:
            basket.append(doll)
    return count