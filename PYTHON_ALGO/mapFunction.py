# map(function, iterable)
# 반환값은 map 객체이므로, list 혹은 tuple 로 변환시켜주어야 한다

import math

a = 'this is my precious'
result_list = list(map(str, a))
print(result_list)
# ['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'm', 'y', ' ', 'p', 'r', 'e', 'c', 'i', 'o', 'u', 's']

test2 = [1.1, 2.2, 3.3, 4.4, 5.5]
result_list2 = list(map(math.ceil, test2))  # ceil 은 올림 함수
print(result_list2)
# [2, 3, 4, 5, 6]

# lambda function 변수 : 조건
result_list3 = list(map(lambda x : x*3, test2))
print(result_list3)
# [3.3000000000000003, 6.6000000000000005, 9.899999999999999, 13.200000000000001, 16.5]