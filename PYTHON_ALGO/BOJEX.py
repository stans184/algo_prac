# 하노이 탑
# 3개의 받침대
# 원판 갯수를 입력받음
# 몇번 움직였는지 출력하고
# 뭐가 어디로 가는지 출력해야함

def move(no, x, y, arr):
    if no>1:
        move(no-1, x, 6-x-y, arr)
    arr[no] = y
    if no>1:
        move(no-1, 6-x-y, y, arr)

plate = int(input())
cnt = dict()
move(plate, 1, 3, cnt)
print(cnt)