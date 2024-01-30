# 정사각형의 크기를 입력 받은 후 시계 방향으로 돌면서 다음과 같은 형태로 출력하는 프로그램을 작성하시오.

# < 처리조건 >
# (1) 가장 왼쪽 위의 좌표부터 차례로 숫자를 대입 시킨다.
# (2) 오른쪽으로 채워 나가다가 끝이면 다시 아래 → 왼쪽 → 위 →오른쪽의 순으로 모두 채워질 때까지 반복한다.

# 예시
# input = 5
# output
# 1 2 3 4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

def fill_square(n):
    # n x n 정사각형 초기화
    square = [[0] * n for _ in range(n)]

    x, y = 0, 0  # 시작 위치
    dx, dy = 0, 1  # 초기 이동 방향 (오른쪽)
    num = 1  # 채울 숫자

    while num <= n*n:
        square[x][y] = num
        num += 1

        # 다음 위치 계산
        if not (0 <= x + dx < n and 0 <= y + dy < n) or square[x + dx][y + dy] != 0:
            # 방향 전환: 오른쪽 → 아래 → 왼쪽 → 위 → 오른쪽
            dx, dy = dy, -dx

        x += dx
        y += dy

    return square

def print_square(square):
    for row in square:
        print(" ".join(map(str, row)))

# 입력
n = int(input())

# 정사각형 채우기
square = fill_square(n)

# 정사각형 출력
print_square(square)