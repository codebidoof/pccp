# heapq
import heapq

heap = []

heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 20)
heapq.heappush(heap, 1)

print(heap)

print(heapq.heappop(heap)) # 출력: 1
print(heap) # [5, 10, 20]
print(heapq.heappop(heap)) # 출력 : 5
print(heap) # [10, 20]