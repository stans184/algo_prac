# https://leetcode.com/problems/trapping-rain-water/

input1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
input2 = [4, 2, 0, 3, 2, 5]

# my code -> wrong

def trap(height):
    stack = []
    max_height = 0
    
    for rain in height:
        if rain == 0:
            if max_height <= sum(stack) and stack:
                max_height = sum(stack)
            stack = []
        elif sum(stack[-1:]) < rain:
            stack.append(rain)
    print(stack)
    max_height = sum(stack)
        
    return max_height


# stack을 활용한 풀이
# 문제에 대한 이해가 잘 안됨
# 일단 적어놓고 스킵
def trap2(height):
    stack = []
    volume = 0
    
    for i in range(len(height)):
        # 변곡점을 만나는 경우
        while stack and height[i] > height[stack[-1]]:
            # 스택에서 꺼낸다
            top =  stack.pop()
            
            if not len(stack): break
            
            # 이전과의 차이 정도만 물 높이 처리
            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]
            
            volume += distance * waters
            
        stack.append(i)
        
    return volume

print(trap2(input1))
print(trap2(input2))