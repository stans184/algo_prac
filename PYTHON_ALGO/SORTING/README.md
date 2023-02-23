# [Selection Sort] (선택 정렬)
# - time complexity O(n^2)
# - 제일 작은 값, 혹은 제일 큰 값을 찾아서 정렬하는 방법
# - index 를 맨 앞에서 시작할때는, 배열의 제일 작은 값을 찾아서 위치를 바꾸고
# - index 가 맨 뒤에서 시작하면, 배열의 제일 큰 값을 찾아서 위치를 바꾼다
#
# [Insert Sort] (삽입 정렬)
# - time complexity O(n^2)
# - 현재 선택된 값의 앞부분을 검사하면서 큰 값아 있으면 자리를 바꾸고
# - index 를 앞으로 옮기면서 계속 검사한다
#
# [Counting Sort] (계수 정렬)
# - time complexity O(n)
# - 타겟 배열의 최대값만한 길이의 counting 배열을 만들고
# - 특정 값이 나올때마다 counting 배열을 하나씩 더해줌
# - counting 배열을 다시 순차적으로 검색하며, 하나 이상 들어가 있으면
# - 그 값을 들어간 갯수 만큼 result 배열로 저장
#
# [Quick Sort]
# - time complexity O(nlogn) // worst O(n^2)
# - 임의의 element 를 pivot 으로 잡고
# - 작은 값을 왼쪽, 큰 값을 오른쪽으로 보내고
# - 그 가운데로 pivot 을 옮긴다
# - 위와 같은 action 을 partition 으로 부르며
# - partition 을 지속접으로 잡아가는 것을 quick sort
#
# [Heap Sort]
# - time complexity O(nlogn)