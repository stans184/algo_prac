# filter(function, iterator)
# iterator 의 값들을 function 으로 처리해서 값이 true 인 요소들만 list 로 리턴

# 1 이상 21 미만의 수 중에서 2로 나눈 나머지가 0인 값들만 filtering
arr1 = list(filter(lambda x : x%2 == 0, range(1,21)))
print(arr1)
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]