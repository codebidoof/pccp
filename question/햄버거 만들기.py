#내 풀이
def solution(ingredient):
    sequence = [1, 2, 3, 1]
    stack = []
    count = 0
    for ing in ingredient:
        stack.append(ing)
        if len(stack) >= 4 and stack[-4:] == sequence:
            count += 1
            for _ in range(4):
                stack.pop()
    return count

#다른 풀이
def solution(ingredient):
    s = []
    cnt = 0
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1, 2, 3, 1]:
            cnt += 1
            for i in range(4):
                s.pop()
    return cnt

#스택문제는 푸시부터 하고보자!!