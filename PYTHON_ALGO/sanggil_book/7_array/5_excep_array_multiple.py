# https://leetcode.com/problems/product-of-array-except-self/
import math

# output[i] = input[i]를 제외한 나머지 input 값들의 곱
# testcase
input1 = [1, 2, 3, 4]
# ans1 [24,12,8,6]
input2 = [-1, 1, 0, -3, 3]
# ans2 [0,0,9,0,0]

# 제약조건
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30

# 도전
# 엄청 큰 숫자가 들어왔을 때 시간초과남
def productExceptSelf(nums):
    out = [1] * len(nums)
    for i in range(len(nums)):
        out[i] = math.prod(nums[0:i] + nums[i+1:len(nums)])
    
    return out

# 1. 왼쪽 곱셈 겨로가에 오른쪽 값을 차례대로 곱셈
