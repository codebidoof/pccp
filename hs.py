import heapq

nums = [34, 27, 19, 51, 8, 24 ,11]

# 음수로 변환해서 최대 힙을 최소 힙처럼 다룸
max_heap = [-n for n in nums]
heapq.heapify(max_heap)
print(max_heap)

# 최대값 꺼내기 (음수로 되어 있으니 다시 양수로 변환)
max_value = -heapq.heappop(max_heap)
print(max_value)  # 출력: 51
print(max_heap)


max_value = -heapq.heappop(max_heap)
print(max_value)
print(max_heap)

max_value = -heapq.heappop(max_heap)
print(max_value)
print(max_heap)

max_value = -heapq.heappop(max_heap)
print(max_value)
print(max_heap)

max_value = -heapq.heappop(max_heap)
print(max_value)
print(max_heap)