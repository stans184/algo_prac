# selection sort
# O(n^2)
# 배열의 앞에서부터 값을 고르고, 뒤의 배열중에 최소값을 찾아서 교환하는 방식

def selectSort(arr):
    for i in range(len(arr)):
        minValue = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minValue]:
                minValue = j
        arr[minValue], arr[i] = arr[i], arr[minValue]
    
    return arr

arr = [80, 50, 70, 10, 60, 20, 40, 30]

print(selectSort(arr))