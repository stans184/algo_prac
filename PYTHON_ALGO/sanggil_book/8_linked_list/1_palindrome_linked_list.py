# https://leetcode.com/problems/palindrome-linked-list/description/

input1 = [1,2,2,1] # true
input2 = [1,2]     # false


# 1. 시도, queue
# 문제에서 제시하는 변수로 받는 head의 타입이 ListNode
# 그냥 반복을 돌리면 돌아가지 않음
import collections
def isPalindrome1(head):
    q = collections.deque()
    # 비었으면 끝내고    
    if not head: return True
    # 안비었으면 넣고
    while head:
        q.append(head.val)
        head = head.next
    # 홀수일경우도 있음
    while len(q) > 1:
        if q.pop() != q.popleft():
            return False

    return True

# 2. 책 보고 참조
def isPalindrome2(head):
    

print(isPalindrome1(input2))