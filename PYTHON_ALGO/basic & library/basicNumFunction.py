import math

# 소수점 올림 ceil
# 소수점 내림 floor
# 반올림 round

a = math.pi

print(a)
print('ceil', math.ceil(a))
print('floor', math.floor(a))
print(round(a))
print(round(a, 2))      # round 함수 뒤에 숫자를 넣어주면 해당하는 소수점 자리까지 반올림 후 반환

# 제곱 pow(x,y)     >   x의 y승 반환
# 제곱근 sqrt

b = 256
print('pow', math.pow(b,2))
print('sqrt', math.sqrt(b))

# 최대공약수 gcd
# 최소공배수 lcm

print(math.gcd(234346,1231234,67867))
print(math.lcm(234,456,12))