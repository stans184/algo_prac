# bubble sort
# time complexity O(n^2)

# 배열의 첫번째 부터 뒤로 쭉 훑으면서, 자기보다 크기를 비교하여 위치를 바꾸는 방식
# 아래 코드 기준, 맨 뒤까지 제일 큰 값을 보내고 그거를 하나씩 앞으로 땡겨온다

def bubbleSort(arr):
    for i in range(len(arr)-1, 0, -1):
    # for i in range(len(arr)):
        for j in range(0,i):
        # for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

data = [10, 55, 23, 2, 79, 101, 16, 82, 30, 45]
print(bubbleSort(data))