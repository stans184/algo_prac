# 정사각형의 크기와 각 숫자를 입력받은 후 시계방향으로 회전하는 프로그램을 작성하시오.

# (1) 키보드를 통해 아래와 같은 크기 n과 각 행의 숫자를 입력받는다. (<표>참고)
# (2) 회전할 각도를 입력받는다. (90, 180, 270, 360)
# (3) 입력받은 배열을 시계방향으로 입력받은 각도만큼 회전하여 출력한다.
# (4) 하나의 회전을 마친 후에는 회전되어진 데이터를 중심으로 다시 각도를 입력받아서 회전한다.
# (5) 0이 입력되면 종료한다

# 예시
# 5
# 3 4 1 2 3
# 2 3 4 5 6
# 2 3 4 6 7
# 1 7 6 5 4
# 6 8 9 3 4
# 90
# 0

# 출력
# 6 1 2 2 3
# 8 7 3 3 4
# 9 6 4 4 1
# 3 5 6 5 2
# 4 4 7 6 3

def rotate_square(matrix, angle):
    if angle == 90:
        return [list(reversed(col)) for col in zip(*matrix)]
    elif angle == 180:
        return [row[::-1] for row in matrix[::-1]]
    elif angle == 270:
        return [list(col) for col in reversed(list(zip(*matrix)))]
    elif angle == 360:
        return matrix
    else:
        return []

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

# 정사각형 크기 입력
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

while True:
    angle = int(input())
    if angle == 0:
        break
    matrix = rotate_square(matrix, angle)
    print_matrix(matrix)