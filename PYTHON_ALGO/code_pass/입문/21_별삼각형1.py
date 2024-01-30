# 삼각형의 높이 n과 종류 m을 입력 받은 후 다음과 같은 삼각형 형태로 출력하는 프로그램을 작성하시오.

# 삼각형의 크기 n(n의 범위는 100 이하의 자연수)과 종류 m(m은 1부터 3사이의 자연수)을 입력받는다.
# 위에서 언급한 3가지 종류를 입력에서 들어온 높이 n과 종류 m에 맞춰서 출력한다.
# 입력된 데이터가 주어진 범위를 벗어나면 "INPUT ERROR!"을 출력한다.

n = int(input("삼각형의 높이를 입력하세요: "))
m = int(input("삼각형의 종류를 입력하세요 (1~3): "))

# 입력된 데이터가 주어진 범위를 벗어나면 에러 메시지 출력
if n > 100 or not 1 <= m <= 3:
    print("INPUT ERROR!")
else:
    if m == 1:
        for i in range(1, n+1):
            print('*' * i)
    elif m == 2:
        for i in range(n, 0, -1):
            print('*' * i)
    elif m == 3:
        for i in range(1, n+1):
            print(' ' * (n - i) + '*' * (2*i - 1))