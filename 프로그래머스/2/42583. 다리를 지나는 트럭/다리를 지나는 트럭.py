from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    
    t = 0
    cur_weight = 0
    
    while trucks or cur_weight > 0:
        t += 1
        cur_weight -= bridge.popleft()
        
        if trucks and cur_weight + trucks[0] <= weight:
            truck = trucks.popleft()
            bridge.append(truck)
            cur_weight += truck
        else:
            bridge.append(0)
    
    return t