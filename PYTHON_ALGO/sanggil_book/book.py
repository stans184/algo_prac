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
