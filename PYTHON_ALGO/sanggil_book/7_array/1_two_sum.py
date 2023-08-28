# https://leetcode.com/problems/two-sum/

nums = [2, 7, 11, 15]
target = 9

# 1) brute force
# 무차별 대입 방식, 비효율적
# 시간 복잡도가 O(n2)ㅇ이다.
# 다른 최적화된 풀이법을 고민해야 함

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

print(twoSum(nums, target))


# 2) in을 이용한 탐색
# nums를 앞에서부터 순환하면서
# target - 현재값 한 값이 남은 배열에 있는지 확인하고
# 있다면 두개를 출력
# in의 시간 복잡도와 for 문이 있으므로 O(n2)

def twoSum2(nums, target):
    for i, n in enumerate(nums):
        check = target - n
        
        if check in nums[i + 1:]:
            return [nums.index(n), nums[i + 1:].index(check) + (i + 1)]
        
print(twoSum2(nums, target))
        

# 3) 해쉬를 이용한 방법
# nums의 index와 값을 hash 함수로 저장
# nums의 앞에서부터 진행하며 target과의 차이값을 nums_hash 에서 찾아본 후,
# 그 값이 있고, 지금 뺀 값의 index가 아니라면 그것이 정답
# 시간 복잡도는 O(n)

def twoSum3(nums, target):
    nums_hash = {}
    
    for i, n in enumerate(nums):
        nums_hash[n] = i
        
    for i, n in enumerate(nums):
        if target - n in nums_hash and i != nums_hash[target - n]:
            return [i, nums_hash[target - n]]
        
print(twoSum3(nums, target))


# 4) two pointer를 이용한 풀이
# 정렬된 상태에서 사용하면 매우 빠르다
# 왼쪽 끝에서 시작하는 포인터 i와 오른쪽 끝에서 시작하는 포인터 j
# 두 포인터가 가리키는 합이 target 값보다 크다면 j를 왼쪽으로
# 합이 target 값보다 작다면 i를 오른쪽으로
# 그런데 이 문제의 경우 정렬을 시켜버리면 index가 다 꼬여버린다