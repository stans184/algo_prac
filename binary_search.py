numList = [12, 25, 31, 48, 54, 66, 70, 83, 95, 108]
# binary search 를 활용하기 위해서는 이미 정렬된 리스트가 필요하다
# target = 83, 88

def binary_search(num, targetList):
    left = 0
    right = len(targetList)-1
    mid = (right + left)//2
    findNum = False

    while (left <= right):
        if targetList[mid] == num:
            findNum = True
            break
        elif num < targetList[mid]:
            right = mid-1
        else:
            left = mid+1
        
        mid = (left + right)//2

    if findNum:
        print(num, "은 ", mid, "에 있습니다.")
    else:
        print(num, "은 리스트에 없습니다.")

binary_search(83, numList)
binary_search(88, numList)