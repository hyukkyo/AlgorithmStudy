from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length, maxlen=bridge_length) # 0으로 초기화
    ready = deque(truck_weights) # 준비된 트럭들
    
    bridge_sum = 0 # 다리 위의 트럭 총 무게

    # 첫번째 트럭을 넣어준다
    if ready:
        bridge_sum = ready.popleft()
        bridge.append(bridge_sum) 
    time = 1

    while True:
         # 다리 위가 0으로 가득차게 되면 종료
        if bridge_sum == 0:
            break

        # 준비된 트럭이 있고, 다리에 트럭이 올라가도 버티면
        if ready and bridge and bridge_sum - bridge[0] + ready[0] <= weight:
            bridge_sum = bridge_sum - bridge[0] + ready[0]
            bridge.append(ready.popleft()) # 다리위로 넣는다. 자연스럽게 bridge에서는 튀어나옴
        else:
            bridge_sum = bridge_sum - bridge.popleft()
            bridge.append(0) # 못버티면 0넣는다
        time += 1

    return time