# https://school.programmers.co.kr/learn/courses/30/lessons/42583

# 강을 가로지르는 하나의 차선으로 된 다리가 하나 있다. 이 다리를 𝑛 개의 트럭이 건너가려고 한다.
# 트럭의 순서는 바꿀 수 없으며, 트럭의 무게는 서로 같지 않을 수 있다. 다리 위에는 단지 𝑤 대의
# 트럭만 동시에 올라갈 수 있다. 다리의 길이는 𝑤 단위길이(unit distance)이며, 각 트럭들은 하나의
# 단위시간(unit time)에 하나의 단위길이만큼만 이동할 수 있다고 가정한다. 동시에 다리 위에 올라가
# 있는 트럭들의 무게의 합은 다리의 최대하중인 𝐿보다 작거나 같아야 한다. 참고로, 다리 위에
# 완전히 올라가지 못한 트럭의 무게는 다리 위의 트럭들의 무게의 합을 계산할 때 포함하지
# 않는다고 가정한다.

# bridge_length	weight	truck_weights	return
# 2	            10	    [7,4,5,6]	    8
# 100	        100	    [10]        	101
# 100	        100	    [10,10,10,10,10,10,10,10,10,10]	110

# 매 초가 갈때마다 진행되는 일
# truck 한대가 bridge로 올라옴
# bridge 위에 truck이 있다면, 1만큼 전진
# bridge length 만큼 전진한 truck이 있다면 내려옴

from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    above_bridge = deque()
    
    while truck_weights or above_bridge:
        # 다리 위에 트럭이 있을 때
        if above_bridge:
            # 가장 왼쪽에 있는 트럭
            first_truck = above_bridge.popleft()
            # 그 트럭이 들어온 시간이 length 만큼 움직이기 전이라면 다시 넣기, 이후라면 그대로 빼버리기
            if time - first_truck[0] < bridge_length:
                above_bridge.appendleft(first_truck)
        
        # 다리위의 트럭의 무게 합이 limit 보다 작다면
        if truck_weights and sum(truck[1] for truck in above_bridge) + truck_weights[0] <= weight:
            # 트럭이 한대 올라옴
            above_bridge.append([time, truck_weights[0]])
            # 원래 대기줄에서는 빠지고
            truck_weights = truck_weights[1:]
        
        time += 1
        
    return time

print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))