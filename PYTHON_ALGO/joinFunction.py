# '구분자'.join(리스트)
# 반복되는 문구를 쉽게 합칠수 있는 함수

a = ['a', 'b', 'c', 'd', '1', '2', '3']
print(a)
print()
 
# 리스트를 문자열로 : join 이용
result1 = "".join(a)
print(result1)

# 원본 리스트
a = ['BlockDMask', 'python', 'join', 'example']
print(a)
print()
 
# 리스트를 문자열로 합치기
result1 = "_".join(a)
print(result1)
 
# 리스트를 문자열로 합치기
result2 = ".".join(a)
print(result2)

# 리스트 출력, for 문 안돌고
# join 은 문자열만 변환이 되므로, 숫자는 안됨
R = {'a','b','c','d','e'}
print("\n".join(sorted(list(R))))

# 문자열로 변환하고 넣으면 되네
t = [5,6,2,4,7,2,4,7,9]
print("\t".join(sorted([str(i) for i in t])))