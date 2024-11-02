from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length, maxlen=bridge_length) # 0으로 초기화
    ready = deque(truck_weights)
    
    # 첫번째 트럭을 넣는다
    if ready:
        bridge_sum = ready.popleft()
        bridge.append(bridge_sum)
    time = 1

    while True:
         # 다리 위가 0으로 가득차면 종료
        if bridge_sum == 0:
            break

        # 준비된 트럭이 있고, 다리에 트럭이 올라가도 버티면
        if ready and bridge_sum - bridge[0] + ready[0] <= weight:
            bridge.append(ready.popleft()) # 다리위로 넣는다
            bridge_sum = bridge_sum - bridge[0] + ready[0]
        else:
            bridge.append(0) # 못버티면 0넣는다
            bridge_sum = bridge_sum - bridge[0]
        time += 1

    return time