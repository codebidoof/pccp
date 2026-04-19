def solution(prices):
    n = len(prices)
    
    stack = [] # 아직 떨어지지 않은 주식의 인덱스만 모아놓는 스택
    answer = [0]*n # [0, 0, 0, 0, 0]
    
    for i, p in enumerate(prices): # 인덱스(현재 시점), 가격 값
        while stack and p < prices[stack[-1]]:
            j = stack.pop() # j = 방금 떨어진 주식의 시점
            answer[j] = i-j # j시점 주식의 가격은 i-j초만큼 안 떨어졌다.
            
        stack.append(i) # 인덱스 값을 스택에 넣음. 인덱스 i = i초 시점
    
    while stack:
        j = stack.pop()
        answer[j] = (n-1)-j # n-1: 마지막 시점, j: 끝까지 안 떨어진 주식의 시점(인덱스)
    return answer