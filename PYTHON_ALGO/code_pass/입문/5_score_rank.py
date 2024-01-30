# 5명의 학생들의 ​수학, 과학점수를 입력받은 후 숫자 N을 입력받아 N이 1이면 수학, 
# 2이면 과학, 3이면 수학+과학 점수가 높은 순으로 학생들의 번호를 출력하는 프로그램을 작성하시오.
# 학생의 번호는 입력받은 순서대로 1부터 매겨진다.

def sort_students(scores, N):
    if N == 1:
        # 수학 점수에 따라 정렬
        sorted_scores = sorted(enumerate(scores), key=lambda x: x[1][0], reverse=True)
    elif N == 2:
        # 과학 점수에 따라 정렬
        sorted_scores = sorted(enumerate(scores), key=lambda x: x[1][1], reverse=True)
    elif N == 3:
        # 수학 + 과학 점수에 따라 정렬
        sorted_scores = sorted(enumerate(scores), key=lambda x: x[1][0] + x[1][1], reverse=True)
    
    # 학생 번호 출력 (1부터 시작하도록 조정)
    for idx, _ in sorted_scores:
        print(idx + 1, end=' ')
    print()

# 5명의 학생 점수 입력
scores = [tuple(map(int, input().split())) for i in range(5)]

# 정렬 기준 입력
N = int(input())

# 학생 정렬 및 출력
sort_students(scores, N)