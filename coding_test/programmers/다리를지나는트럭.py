from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    answer, i, truck_count = 0, 0, len(truck_weights)
    
    while len(bridge):
        weight += bridge.popleft()

        if i < truck_count:
            if weight >= truck_weights[i]:
                bridge.append(truck_weights[i])
                weight -= truck_weights[i]
                i += 1
            else:
                bridge.append(0)

        answer += 1
        # print(answer, bridge, weight)
    return answer

print(solution(2, 10, [7,4,5,6]))
# print(solution(100, 100, [10]))
# print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
