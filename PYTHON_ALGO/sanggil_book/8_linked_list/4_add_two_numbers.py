# https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# 1. LinkedList > list > LinkedList
class Solution:
    # LinkedList 뒤집기
    def reverseList(self, head):
        node, prev = head, None
        
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
            
        return prev
    
    # list로 변환
    def toList(self, node):
        list = []
        while node:
            list.append(node.val)
            node = node.next
        return list
    
    # LinkedList로
    def toReversedLinkedList(self, result):
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node

    def addTwoNumbers(self, l1, l2):
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))
        
        resultStr = int(''.join(str(e) for e in a)) + \
                    int(''.join(str(e) for e in b))
                    
        return self.toReversedLinkedList(str(resultStr))
        