class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 연결 리스트 클래스 만들기
class LinkedList:
    def __init__(self):
        self.head = None #공백 리스트 생성
        self.length = 0

    def __len__(self): #길이 계산 메서드
        return self.length
    
    def appendleft(self, data): #왼쪽에다 노드삽입
        if self.head is None: #공백일 경우
            self.head = Node(data) #헤드 포인터가 새 노드를 가리킨다
        else:
            new = Node(data) # 삽입할 노드 생성하고 뉴 포인터가 가리키게 함
            new.next = self.head # 새노드의 링크필드에 기존 첫번째 노드 주소 설정
            self.head = new # 헤드 포인터가 새 노드를 가리키도록 함
        self.length += 1 # 길이 증가

    def append(self, data): #오른쪽에다 노드삽입
        if self.head is None: #공백일 경우
            self.head = Node(data)  
        else:
            temp = self.head  #temp는 탐색하는 포인터 역할, 첫 노드를 가리키게 초기화
            while temp.next is not None: # 끝에 갈때까지
                temp = temp.next #다음 노드로 이동
            temp.next = Node(data) #노드 삽입
        self.length += 1 #길이 증가

    def __str__(self): #연결 리스트 상태 출력하기
        if self.head is None:
            return "Linked list is empty!"
        res = "Head"
        temp = self.head
        while temp is not None:
            res += " -> " + str(temp.data)
            temp = temp.next
        return res

    def __contains__(self, target): #값이 포함되어있는지 확인하는 메서드
        if self.head is None: #공백일 경우
            return False
        temp = self.head 
        while temp is not None:
            if temp.data == target:
                return True
            temp = temp.next
        return False
    
    def popleft(self): #왼쪽에서 삭제
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        self.length -= 1
        return temp.data
    
    def pop(self): #오른쪽에서 삭제
        if self.head is None:
            return None
        temp = self.head
        while temp.next is not None:
            prev = temp
            temp = temp.next
        if temp == self.head:
            self.head = None
        else:
            prev.next = None
        self.length -= 1
        return temp.data
    
    def remove(self, target): # 특정 노드 삭제
        temp = self.head
        while temp is not None and temp.data != target:
            prev = temp
            temp = temp.next
        if temp is None:
            return False
        if temp == self.head: #삭제할 노드가 head인 경우
            self.head = self.head.next
        else:
            prev.next = temp.next
        self.length -= 1
        return True
    
    def insert(self, i, data): #특정 위치(i)에 데이터를 삽입
        if i <= 0:
            self.appendleft(data)
        elif i >= self.length:
            self.append(data)
        else:
            temp = self.head
            for _ in range(i-1):
                temp = temp.next
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node
        self.length += 1

    def reverse(self): #연결리스트 뒤집기
        if self.length < 2:
            return
        p = self.head
        q = None
        r = None

        # 리스트의 첫 번째 노드부터 링크를 따라 다음 노드로 이동하면서 노드 간의 연결을 바꿈
        while p is not None:
            r = q
            q = p
            p = p.next
            q.next = r
        self.head = q





if __name__ == "__main__":
    import random
    data = list(range(10, 15))
    random.shuffle(data)
    my_list = LinkedList()
    for i in data:
        my_list.append(i)
    print(f"연결 리스트의 상태\n연결 리스트의 길이 =  {len(my_list)},  {my_list}")
    print()
    for _ in range(10):
        i = random.randint(10, 15)
        if my_list.remove(i):
            print(f"{i}를 연결 리스트에서 삭제했습니다.")
            print(f"연결 리스트의 길이 = {len(my_list)},  {my_list}\n")
        else:
            print(f"{i}는 연결 리스트에 없습니다.\n")
    