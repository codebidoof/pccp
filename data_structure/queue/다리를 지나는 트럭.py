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
    pass

