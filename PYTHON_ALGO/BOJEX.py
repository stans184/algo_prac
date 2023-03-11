# 10 2
# 3 -2 -4 -9 0 3 7 13 8 -3

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
sum_list = []

pre_sum = sum(arr[:k])
sum_list.append(pre_sum)

for i in range(len(arr)-k):
    pre_sum = pre_sum + arr[i+k] - arr[i]
    sum_list.append(pre_sum)

print(max(sum_list))