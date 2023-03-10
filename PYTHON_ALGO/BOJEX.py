# 하노이 탑
# 3개의 받침대
# 원판 갯수를 입력받음
# 몇번 움직였는지 출력하고
# 뭐가 어디로 가는지 출력해야함

# def move(no, x, y, arr):
#     if no>1:
#         move(no-1, x, 6-x-y, arr)
#     arr.append([x, y])
#     if no>1:
#         move(no-1, 6-x-y, y, arr)

# plate = int(input())
# cnt = []
# move(plate, 1, 3, cnt)
# print(len(cnt))
# for content in cnt:
#     print(content[0], content[1])

import sys, itertools

input = sys.stdin.readline

m,n = map(int, input().split())

ans = list(itertools.combinations_with_replacement(range(1,m+1), n))

for check in ans:
    for num in check:
        print(num, end=" ")
    print()