def rotate(s):
    return s[1:]+s[0] #슬라이싱을 통한 회전

def is_pair(c, stack):
    if not stack:
        return False
    else: 
        temp = stack.pop() + c
        if (temp == "[]" or temp == "{}" or temp == "()"):
            return True
        else:
            return False
    
def solution(s):
    x = 0
    stack = []
    count = 0 #문자열의 끝까지 다 순회하였는지 체크하는 변수
    for _ in range(len(s)):
        for c in s:
            if c == "[" or c=="(" or c=="{":
                stack.append(c)
                count += 1
                continue
            elif c == "]" or c==")" or c=="}":
                if not is_pair(c, stack): #짝이 안 맞을때 문자열을 순회하는 반복문 탈출
                    break
                else: #짝이 맞으면 count를 1 증가시키고 다음 문자로 넘어감
                    count += 1  
                    continue
        if count==len(s) and not stack: 
            x += 1
        count = 0 #다음 사이클 시작 전 count값 초기화
        stack.clear() #스택 상태 초기화
        s = rotate(s) #문자열 회전
    return x