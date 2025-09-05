#1. 데크 사용
from collections import deque

def solution(slot_times, k):
    queue = deque([(i+1, t) for i, t in enumerate(slot_times)]) # (슬롯 번호, 남은 시간)
    while k > 0 and queue:
        slot_num, time = queue.popleft()
        # 남은 시간이 0이라면 팝하고 끝
        if time > 0:
            time -= 1
            k -= 1

            if time > 0: # 남은 시간이 있다면 다시 뒤에 넣음
                queue.append((slot_num, time))

    if queue:
        return queue[0][0]  # 다음에 충전할 슬롯 번호
    else:
        return -1
    
# 2. 우선순위 큐(최소 큐) 사용
import heapq

def solution2(slot_times, k):
    if sum(slot_times) <= k: 
        return -1

    que = []
    for i in range(len(slot_times)):
        heapq.heappush(que, (slot_times[i], i + 1)) # (남은 시간, 슬롯 번호)

    prev = 0 # 이전 단계에서 삭제한 노드의 시간값
    length = len(slot_times) # 충전 슬롯의 개수

    while (que[0][0] - prev) * length < k:
        k -= (que[0][0] - prev) * length
        length -= 1
        prev, prev_num = heapq.heappop(que)

    result = sorted(que, key=lambda x: x[1]) # 슬롯 번호순으로 정렬
    return result[k % length][1]

# 테스트 케이스
slot_times = [3, 1, 2]
k = 5
print(solution(slot_times, k))
print(solution2(slot_times, k))

