# str.isdisit()     >      문자열에 들어있는 값이 숫자인지 판단
# str.isalpha()     >      문자열에 들어있는 값이 글자인지 판단
# str.isdecimal()
# str.isnumeric()

a = '1234'
print(a.isdigit())
print(a.isalpha())
print(a.isdecimal())

# ord(문자)             'A' = 아스키코드 65, 'a' = 아스키코드 97
print(ord('a'))
print(ord('A'))
print(chr(ord('A') + 32))
# chr(정수)
print(chr(98))

# 삼항 연산자
# [True 일때 실행값] if [condition] else [False 일때 실행값]

print(True if 4%2 == 0 else False)