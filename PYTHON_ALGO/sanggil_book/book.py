import collections

import this

a = [1, 2, 3, 34, 45, 56, 7, 1, 2, 3, 3, 1]

print(a)

print(list(enumerate(a)))

print(divmod(345, 32))

print(type(this))

is_duple = True

print(is_duple)

for i in range(10, 12):
    x = i
    y = x
    print(id(i), id(x), id(y))

# is 는 id() 값을 비교하는 연산자
# == 은 값을 비교하는 연산자

# =========================================
# list 와 dictionary 정리 필요

b = collections.Counter(a)
print(b)  # Counter({1: 2, 2: 1, 3: 1, 34: 1, 45: 1, 56: 1, 7: 1})
print(b.most_common(2))

# =========================================
# python의 sort() 함수와 sorted() 함수는 timsort 정렬을 사용한다
# timsort 정렬은 insert sort 와 merge sort 를 섞은 것이다
# 최고 O(n) 안정 O(nlogn) 최악 O(nlogn) 의 성능을 발휘한다
# 현업에서도 가장 많이 쓰이는 정렬 알고리즘
# 파이썬을 통해 문제를 해결할 떄, 엥간하면 이게 제일 빠르다
