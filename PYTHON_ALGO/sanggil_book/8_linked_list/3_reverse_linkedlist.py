# https://leetcode.com/problems/reverse-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def listToLinkedlist(list):
    if not list: return None
    head = ListNode(list[0])
    current_node = head
    
    for val in list[1:]:
        current_node.next = ListNode(val)
        current_node = current_node.next
    return head

def printLinkedList(list):
    current_node = list
    while current_node:
        print(current_node.val, end=' ')
        current_node = current_node.next
    print('', end=' ')
    

head1 = listToLinkedlist([1,2,3,4,5])
# [5,4,3,2,1]
head2 = listToLinkedlist([1,2])
# [2,1]
head3 = listToLinkedlist([])
# []


# 1. 책, 재귀
def reverseList1(head):
    return None
    

# 2. 책, 반복문
def reverseList2(head):
    node, prev = head, None
    
    while node:
        print('node : ', end='')
        printLinkedList(node)
        print()
        print('prev : ', end='')
        printLinkedList(prev)
        print()
        next, node.next = node.next, prev
        prev, node = node, next
        print('node : ', end='')
        printLinkedList(node)
        print()
        print('prev : ', end='')
        printLinkedList(prev)
        print()
        print()
    
    return prev

print(printLinkedList(reverseList2(head1)))