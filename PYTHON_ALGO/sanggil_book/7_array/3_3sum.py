# https://leetcode.com/problems/3sum/
# 세 수의 합이 0이 되는 숫자들을 모아서 출력하라

nums1 = [-1,0,1,2,-1,-4]
out1 = [[-1,-1,2],[-1,0,1]]
nums2 = [0,1,1]
out2 = []
nums3 = [0,0,0]
out3 = [[0,0,0]]

# 1) brute force
# 3개의 숫자이므로 배열을 3번 반복해야 한다
# O(n3)으로 시간 초과되어 실패

def sol1(nums):
    results = []
    nums.sort()
    
    # brute force n^3번 반복
    for i in range(len(nums) - 2): # j, k 가 들어와야 하니 2개 제외
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i-1]: continue
        for j in range(i+1, len(nums) - 1): # k 가 들어와야 하니 1개 제외
            # 중복값 건너뛰기
            if j > i + 1 and nums[j] == nums[j-1]: continue
            for k in range(j+1, len(nums)):
                if k > j+1 and nums[k] == nums[k-1]: continue
                if nums[i] + nums[j] + nums[k] == 0:
                    results.append([nums[i], nums[j], nums[k]])
                    
    return results

print(sol1(nums1))

# 2) two pointer를 활용한 진행
# 요거도 우선 정렬이 되어야 함
# python list의 sort() 함수는 생각보다 성능이 좋다 -> O(nlogn)

def sol2(nums):
    results = []
    nums.sort()
    
    for i in range(len(nums) - 2):
        if i>0 and nums[i] == nums[i-1]: continue
        
        # 간격을 좁혀가면서 합 계산
        left, right = i+1, len(nums)-1
        
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            
            # nums는 정렬되어 있으므로
            if sum < 0: left += 1
            elif sum > 0: right -= 1
            else:
                results.append([nums[i], nums[left], nums[right]])
                
                # 중복된 숫자가 있다면 건너뛰어야 하므로
                while left < right and nums[left] == nums[left+1]: left += 1
                while left < right and nums[right] == nums[right-1]: right -= 1
                
                # 원래는 sum이 0일때 results에 바로 넣고 한칸씩 옮기면 된다
                left += 1
                right -= 1
    
    return results

print(sol2(nums1))