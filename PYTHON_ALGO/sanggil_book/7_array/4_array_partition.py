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
    print(nums)
    # 동등한 개수의 짝이 있어야 하면서, 최소한으로 나누면 좋다
    n = 2
    print(n)
    ans = 0

    for i in range(0, len(nums), n):
        data = []
        for k in range(n):
            if i+k < len(nums):
                data.append(nums[i+k])
        if len(data) == n: ans += min(data)
        
    return ans