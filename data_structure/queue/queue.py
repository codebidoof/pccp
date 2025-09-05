# 1. 리스트를 큐처럼 활용하기 
queue = []

queue.append(1)
queue.append(2)
queue.append(3)

first_item = queue.pop(0) # 인덱스 0번 출력
print(first_item) # 출력 : 1

queue.append(4)
queue.append(5)

first_item = queue.pop(0)
print(first_item) # 출력 : 2

#2. 덱을 큐처럼 활용하기 - 시간복잡도 낮음
from collections import deque

que = deque() 
que.append(1)
que.append(2)
que.append(3) # deque([1, 2, 3])

first_item = que.popleft() 
print(first_item) # 1

que.append(4)
que.append(5)

first_item = que.popleft()
print(first_item) # 2

# heapq
import heapq

heap = []

heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 20)
heapq.heappush(heap, 1)

print(heap)
