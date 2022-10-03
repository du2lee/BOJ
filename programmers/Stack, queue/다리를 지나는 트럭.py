def solution(bridge_length, weight, truck_weights):
    answer = 0
    truckOnBridge = [0] * bridge_length
    
    while len(truck_weights):
        answer += 1
        truckOnBridge.pop(0)
        if sum(truckOnBridge) + truck_weights[0] <= weight:
            truckOnBridge.append(truck_weights.pop(0))
        else:
            truckOnBridge.append(0)
            
        if truck_weights and truck_weights[0] > weight:
            truck_weights.pop(0)
            answer += bridge_length

    return answer + bridge_length