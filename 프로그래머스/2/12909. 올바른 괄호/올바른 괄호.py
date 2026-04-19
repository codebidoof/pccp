def solution(s):
    stack = []
    for c in s:
        if c=="(":
            stack.append(c)
        else:  # ")" 인 경우
            if not stack: #스택이 공백일 경우
                return False
            else: # ")" 차례일 때 스택이 공백이 아니라면
                stack.pop()
    
    return not stack
    