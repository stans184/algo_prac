# https://leetcode.com/problems/array-partition/

# n개의 짝을 이용해서 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 구해라
input1 = [1, 4, 3, 2]
output2 = 4
input2 = [6, 2, 6, 5, 1, 2]
output2 = 9

# 풀리긴 했는데, 속도와 메모리를 더 아끼는 방향으로 확인해보기
def arrayPairSum(nums):
    # 내림차순 정렬
    nums.sort(reverse=True)
    # 동등한 개수의 짝이 있어야 하면서, 최소한으로 나누면 좋다
    n = 2
    ans = 0

    for i in range(0, len(nums), n):
        data = []
        for k in range(n):
            if i+k < len(nums):
                data.append(nums[i+k])
        if len(data) == n: ans += min(data)
        
    return ans

# 1. 오름차순 풀이
def sol1(nums):
    sum = 0
    pair = []
    nums.sort()
    
    for n in nums:
        # 앞에서부터 오름차순으로 페어를 만들면서 합 계산
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []
            
    return sum

# 2. 짝수 번째 합 계산
# 어차피 2개씩 모아서 비교를 해야함
# 그래야 가장 많은 횟수를 비교해서 총 합을 늘려갈 수가 있음
# 어차피 정렬된 상태에서는 홀수 값보다 짝수 값이 항상 작은 값이다
def sol2(nums):
    sum = 0
    nums.sort()
    
    for i, n in enumerate(nums):
        # 짝수 번째 값의 합 계산
        if i % 2 == 0:
            sum += n
            
    return sum

# 3. 파이써닉한 방법
def sol3(nums):
    return sum(sorted(nums)[::2])