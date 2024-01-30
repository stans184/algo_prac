# 삼각형의 높이 N을 입력받아서 아래와 같이 숫자 0부터 달팽이 모양으로 차례대로 채워진 삼각형을 출력하는 프로그램을 작성하시오.

# < 처리조건 > 
# 왼쪽 위부터 시계방향으로 오른쪽 아래로 이동하면서 숫자 0부터 N개를 채우고 
# 다시 왼쪽으로, 다음은 위쪽으로 반복하면서 채워 나간다. (숫자 9 다음에는 0부터 다시 시작한다.)

# 예시
# input = 6
# output
# 0
# 4 1
# 3 5 2
# 2 0 6 3
# 1 9 8 7 4
# 0 9 8 7 6 5

def fill_triangle(n):
    # 삼각형 초기화
    triangle = [[0 for _ in range(i+1)] for i in range(n)]

    x, y = 0, 0  # 시작 위치
    num = 0  # 채울 숫자

    for _ in range(n):
        # 오른쪽 아래로 이동
        for _ in range(n - x):
            triangle[x][y] = num % 10
            num += 1
            x += 1
            if x < n:
                y += 1

        # 왼쪽으로 이동
        x -= 1
        y -= 2
        for _ in range(n - x - 1):
            triangle[x][y] = num % 10
            num += 1
            x -= 1
            y -= 1

        # 위로 이동
        x += 2
        y += 1
        for _ in range(n - x):
            triangle[x][y] = num % 10
            num += 1
            y += 1

    return triangle

def print_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)))

# 입력
n = int(input("삼각형의 높이를 입력하세요: "))

# 삼각형 채우기
triangle = fill_triangle(n)

# 삼각형 출력
print_triangle(triangle)