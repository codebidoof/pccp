stack = [] #스택 리스트 초기화
max_size = 10

def isFull(stack):
    # 스택이 가득 찼는지 확인하는 함수
    return len(stack) == max_size

def isEmpty(stack):
    # 스택이 비어 있는지 확인하는 함수
    return len(stack) == 0

def push(stack, item):
    # 스택에 데이터를 추가하는 함수
    if isFull(stack):
        print("스택이 가득 찼습니다.")
    else:
        stack.append(item)
        print("데이터가 추가되엇습니다.")

def pop(stack):
    if isEmpty(stack):
        print("스택이 비어 있습니다.")
        return None
    else:
        return stack.pop()
    
a = min(i for i in range(8))
print(a)