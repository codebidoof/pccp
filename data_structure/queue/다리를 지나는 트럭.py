from collections import deque
#내가 작성한 거 - 중간에 포기 ㅠㅠ
def solution(bridge_length, weight, truck_weights):
    duration = bridge_length # 트럭 하나가 다리를 주파하는데 걸리는시간
    my_dict = {x: 0 for x in truck_weights} 
    trucks = deque(truck_weights)
    bridge = deque()
    second = 0 # 현재 시간
    while trucks:            
        temp = trucks.popleft()
        if temp + sum(bridge) < weight: # 하중을 감당 가능할 경우
            bridge.append(temp)
        else:
            trucks.appendleft(temp) # 다시 집어넣음
        
        second += 1
    return second

#타인의 풀이 - 브릿지의 길이만큼의 브릿지 리스트를 만듦 -> 트럭 하나하나 각각 시간을 잴 필요가 없다!
def solution(bridge_length, weight, truck_weights):
    time = 0
    # 데크(큐)로 변환
    bridge = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)

    currentWeight = 0
    while len(truck_weights) != 0:
        time += 1

        currentWeight -= bridge.popleft()

        if currentWeight + truck_weights[0] <= weight:
            currentWeight += truck_weights[0]
            bridge.append(truck_weights.popleft())
        else:
            bridge.append(0)

        time += bridge_length # 후처리

        return time


