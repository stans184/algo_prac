# counting sort <계수 정렬>
# O(n)
# 비교 정렬이 아님, 각 요소의 개수를 더하고
# 배열 요소가 몇번 등장했는지 확인하는 작업이 필요한데
# 이 과정 때문에 배열의 최대값이 지나치게 커지면 정렬 시간이 오래 걸린다는 단점이 있다

def countingSort(arr):
    # 몇번 등장했는지 세기 위한 임의의 배열
    count = [0] * (max(arr) + 1)
    # 숫자가 등장할때마다 세주기
    for i in range(len(arr)):
        count[arr[i]] += 1
    print(count)
    # 저장해서 출력할 리스트
    result = []
    
    for i in range(len(count)):
        # counting 된 index 에는 1이 있고, 아닌 곳엔 0 이 있을 것이다
        # 0 인 곳에서는 append 가 실행되지 않고, 1이 들어가 있는곳에서 append 가 실행된다
        # 그래서 앞에서부터 순서대로 result 에 담기게 되는 것
        for j in range(count[i]):
            result.append(i)
        # if count[i] != 0:
        #     for j in range(count[i]):
        #         result.append(i)
    return result

# data = [10, 55, 23, 2, 79, 101, 16, 82, 30, 45]
data = [6,10,21,12,6,17]

print(countingSort(data))