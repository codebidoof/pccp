from collections import deque

def solution(N, K) : # 회전하는 느낌으로!
    queue = deque(range(1, N + 1)) # 1 2 ... N

    while len(queue) > 1:
        for _ in range(K-1):
            queue.append(queue.popleft())
        queue.popleft()
    return queue[0]


