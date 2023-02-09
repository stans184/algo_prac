# ==========================================
# heap library 사용 예제 (min heap)
# 작은 값부터 정렬
# heap 을 통해 구현 (min heap, max heap)
# heap 은 데이터를 삽입하고, 삭제하는데 O(logN) 이 소요됨    //   리스트로 하면 삽입 O(1), 삭제 O(N)
# ==========================================
# 파이썬에서 제공하는 최소 heap library
import heapq
# 오름차순 heap 정렬
def heapSort(iterable):     # iterable > list, tuple 등
    # heap 을 넣을 배열을 열어둠
    h = []
    # 최종 정렬될 result 배열
    result = []
    # 모든 원소를 그냥 앞에서부터 heap 에 넣고
    for value in iterable:
        # heappush 데이터를 넣고, 조회해보니 넣으면서 아예 정렬됨
        heapq.heappush(h, value)
    # heap 에 삽입된 원소들을 차례대로 꺼내기
    for i in range(len(h)):
        # heappop 데이터를 빼고
        result.append(heapq.heappop(h))
    return result

# 최대 힙은 따로 제공되지 않는다
def heapSort2(iterable):
    h = []
    result = []
    for value in iterable:
        # heap 에 넣기 전에 부호를 바꿔서 넣고
        heapq.heappush(h, -value)
    for i in range(len(h)):
        # 출력할 때 부호를 다시 바꿔주면 내림차순 정렬
        result.append(-heapq.heappop(h))
    return result

# 오름차순 결과
print(heapSort([10, 55, 23, 2, 79, 101, 16, 82, 30, 45]))
# 내림차순 결과
print(heapSort2([10, 55, 23, 2, 79, 101, 16, 82, 30, 45]))