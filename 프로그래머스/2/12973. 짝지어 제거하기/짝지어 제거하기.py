def solution(s):
    stack = [] # 알파벳들 담을 스택 초기화
    
    for c in s: 
        if stack and stack[-1] == c: # 스택이 공백이 아니고 top == 현재문자라면  
            stack.pop() # 팝
        else:
            stack.append(c)
            
    return 1 if not stack else 0 # 스택이 공백이면 1 아니면 0 반환