# 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다
# 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.
# example input 216, output 198

# 0213 하다맘
n = int(input())
ans = 198

for i in range(n):
    result = i


    if result == ans:
        print(result)
        break