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

# 2) two pointer를 활용한 진행
# 요거도 우선 정렬이 되어야 함
# python list의 sort() 함수는 생각보다 성능이 좋다 -> O(nlogn)

