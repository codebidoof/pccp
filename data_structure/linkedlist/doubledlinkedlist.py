class Node: #노드 초기화
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList: #이중연결리스트 클래스
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self): #길이 구하기
        return self.length

    def appendleft(self, data): #왼쪽에 삽입
        new_node = Node(data) #새 노드 생성
        if self.head: # 노드가 하나라도 있다면
            self.head.prev = new_node #헤드 노드의 전 노드를 새 노드로 설정
            new_node.next = self.head #새 노드의 다음 노드를 헤드 노드로 설정
        self.head = new_node # 헤드 업데이트 
        self.length += 1 # 길이 1 증가

    def append(self, data):
        new_node = Node(data)
        if self.head is None: #공백일 경우
            self.head = new_node # 헤드포인터를 새 노드로
        else:
            temp = self.head 
            while temp.next: #다음 노드가 존재할 때까지
                temp = temp.next # 다음 노드로 이동
            temp.next = new_node # 현재 노드의 왼쪽 링크 필드에 새 노드 연결
            new_node.prev = temp 
        self.length += 1

    def popleft(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        self.length -= 1
        return data

    def pop(self):
        if self.head is None:
            return None
        temp = self.head
        if temp.next is None:  # 노드가 하나뿐
            data = temp.data
            self.head = None
            self.length -= 1
            return data
        while temp.next:
            temp = temp.next
        data = temp.data
        temp.prev.next = None
        self.length -= 1
        return data

    def remove(self, target):
        temp = self.head
        while temp and temp.data != target:
            temp = temp.next
        if temp is None:
            return False
        if temp.prev:
            temp.prev.next = temp.next
        else:  # head 노드인 경우
            self.head = temp.next
        if temp.next:
            temp.next.prev = temp.prev
        self.length -= 1
        return True

    def insert(self, i, data):
        if i <= 0:
            self.appendleft(data)
        elif i >= self.length:
            self.append(data)
        else:
            new_node = Node(data)
            temp = self.head
            for _ in range(i):
                temp = temp.next
            prev_node = temp.prev
            new_node.prev = prev_node
            new_node.next = temp
            if prev_node:
                prev_node.next = new_node
            temp.prev = new_node
            self.length += 1

    def reverse(self):
        if self.length < 2:
            return
        current = self.head
        prev_node = None
        while current:
            current.prev, current.next = current.next, current.prev
            prev_node = current
            current = current.prev  # 원래 next였던 방향
        self.head = prev_node

    def __contains__(self, target):
        temp = self.head
        while temp:
            if temp.data == target:
                return True
            temp = temp.next
        return False

    def __str__(self):
        if self.head is None:
            return "Doubly linked list is empty!"
        res = "Head"
        temp = self.head
        while temp:
            res += f" <-> {temp.data}"
            temp = temp.next
        return res
