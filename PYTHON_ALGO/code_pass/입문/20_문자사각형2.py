# 정사각형의 한 변의 길이 n을 입력받은 후 다음과 같은 문자로 된 정사각형 형태로 출력하는 프로그램을 작성하시오.

# < 처리조건 >
# 문자의 진행 순서는 왼쪽 위에서부터 아래쪽으로 ‘A'부터 차례대로 채워나가고 
# 다시 오른쪽 아래부터 위쪽으로 채워나가는 방법으로 아래 표와 같이 채워 넣는다.
# 'Z' 다음에는 다시 'A'부터 반복된다.

# 정사각형 한 변의 길이 n(n의 범위는 1이상 100 이하의 정수)을 입력받는다.
# 위의 형식과 같이 한변의 길이가 n인 숫자 사각형을 출력한다. 숫자 사이는 공백으로 구분하여 출력한다.

# 정사각형 한 변의 길이 n 입력 받기
n = int(input("정사각형 한 변의 길이를 입력하세요: "))

# 문자 정사각형 초기화
square = [[' ' for _ in range(n)] for _ in range(n)]

# 문자 채우기
char_code = ord('A')
for j in range(n):
    if j % 2 == 0:
        for i in range(n):
            square[i][j] = chr(char_code)
            char_code = (char_code - ord('A') + 1) % 26 + ord('A')
    else:
        for i in range(n-1, -1, -1):
            square[i][j] = chr(char_code)
            char_code = (char_code - ord('A') + 1) % 26 + ord('A')

# 문자 정사각형 출력
for row in square:
    print(' '.join(row))