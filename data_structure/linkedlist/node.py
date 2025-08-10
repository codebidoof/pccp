class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

node = head # 제발 되라....ㅠㅠㅠ

# 연결 리스트의 값 출력하기
while node: # Node is not None
    print(node.data, end=" ")
    node = node.next 

# 연결 리스트의 끝에 새 노드를 추가하기
node = head
while node.next:
    node = node.next 
node.next = Node(4)

# 연결 리스트의 처음에 새 노드를 추가하기
new = Node(0)
node.next = head
head = new

# 연결 리스트 클래스 만들기
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length
    
    def appendleft(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = Node(data)
            node.next = self.head
            self.head = None
        self.length += 1
