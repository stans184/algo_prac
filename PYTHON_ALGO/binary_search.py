numList = [12, 25, 31, 48, 54, 66, 70, 83, 95, 108]
# binary search 를 활용하기 위해서는 이미 정렬된 리스트가 필요하다
# target = 83, 88

def binary_search(num, targetList):
    # 가장 왼쪽과
    left = 0
    # 가장 오른쪽을 잡고
    right = len(targetList)-1
    # 가운데 값도 잡아줌
    mid = (right + left)//2
    findNum = False
    # search 범위의 왼쪽 값과 오른쪽 값이 바뀌지 않는 한도에서
    while (left <= right):
        # 만약 가운데 값에 타겟이라면, break
        if targetList[mid] == num:
            findNum = True
            break
        # 찾는 값이 mid 보다 작다면 mid 왼쪽으로 오른쪽 limit 을 옮김
        elif num < targetList[mid]:
            right = mid-1
        # 찾는 값이 mid 보다 크다면 mid 오른쪽으로 left 를 옮김
        else:
            left = mid+1
        
        mid = (left + right)//2

    if findNum:
        print(num, "은 ", mid, "에 있습니다.")
    else:
        print(num, "은 리스트에 없습니다.")

binary_search(83, numList)
binary_search(88, numList)