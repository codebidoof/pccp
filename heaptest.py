import heapq

l1 = [2, 4, 45, 33, 7, 99, 1]
heapq.heapify(l1) # 최소 힙 구성

l2 = [1, 2, 4, 33, 7, 99, 45] 
heapq.heapify(l2) # 최소 힙 구성

print(l1)
print(l2)

# 출력값이 왜 다르지..?
