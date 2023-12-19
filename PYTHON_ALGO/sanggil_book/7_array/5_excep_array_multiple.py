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

# 1. 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈 (try - fail)
# 오른쪽 값을 구하는 과정에서 O(n2) 발생, 시간초과
def productExceptSelf2(nums):
    out = [1] * len(nums)
    # 왼쪽 값들 모두 곱해서 넣음
    for i in range(1, len(nums)):
        for j in range(0, i):
            out[i] *= nums[j]
    # 오른쪽 값들 모두 곱해서 넣음
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            out[i] *= nums[j]
    return out

# 2. 왼쪽 곱셉 배열, 오른쪽 곱셉 배열 따로 구해서 곱하기
def productExceptSelf3(nums):
    length = len(nums)
    
    left, right = [1] * length, [1] * length
    out = [1] * length
    
    # 왼쪽 곱셉
    for i in range(1, length):
        left[i] = nums[i-1] * left[i-1]
        
    # 오른쪽 곱셈
    for i in range(length-2, -1, -1):
        right[i] = nums[i+1] * right[i+1]
    
    # 둘의 곱
    for i in range(length):
        out[i] = left[i] * right[i]
    
    return out

# 3. 책, 왼쪽부터 구하고, 오른쪽을 그 결과에 곱하기
# 제일 시간적 효율이 좋음
# 과정을 간단하게 진행할수록 좋다
def productExceptSelf4(nums):
    out = []
    # indicator, 곱한 값을 저장하는 변수
    p = 1
    # 왼쪽부터
    for i in range(len(nums)):
        out.append(p)
        p *= nums[i]
    # 오른쪽 진행
    # indicator initial
    p = 1
    for i in range(len(nums)-1, -1, -1):
        out[i] *= p
        p *= nums[i]
    
    return out

print(productExceptSelf4(input2))