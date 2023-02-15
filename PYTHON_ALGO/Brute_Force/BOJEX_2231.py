# 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다
# 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.
# example input 216, output 198

n = int(input())
result = 0

for i in range(n):
    # 각 자리수를 뽑아야함
    # 정수를 문자열로 바꾸고, 그것을 map 시켜서 list 로 변환
    num_list = list(map(int, str(i)))
    result = i + sum(num_list)
    if n == result:
        print(i)
        break
    if i == n-1:
        print(0)
        break