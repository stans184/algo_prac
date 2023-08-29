# https://school.programmers.co.kr/learn/courses/30/lessons/42747

citations = [3, 0, 6, 1, 5]  # result 3

def sol1(papers):
    papers.sort(reverse=True)
    
    for i in range(len(papers)):
        if papers[i] <= len(papers[:i]):
            return i
    return len(papers)

# 내림차순으로 정렬 하고 -> O(nlogn)
# 첫번재 값부터 진행
# 현재 값을 h값이라고 하면, 배열[:현재값] <- 현재값을 제외한 이전 값들 (즉, h값보다 큰 값들) 의 크기가 h이상일 때
# return h
# ->> [5,5,5,5] 의 경우와 같이, 들어있는 값들로 h-index를 구별할 수 없는 예외 경우가 있었음

print(sol1(citations))
print()
test1 = [1,1,1,1,1]

print(sol1(test1))
print()
test2 = [3,4,5,1,8,5,3]
print(sol1(test2))
print()

test3 = [1,2,43,3,5,5,5]
print(sol1(test3))