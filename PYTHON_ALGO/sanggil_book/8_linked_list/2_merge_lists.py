# https://leetcode.com/problems/merge-two-sorted-lists/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def listToLinkedList(list):
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

list1 = listToLinkedList([1,2,4]) 
list2 = listToLinkedList([1,3,4])      # [1,1,2,3,4,4]
list3 = listToLinkedList([])
list4 = listToLinkedList([])           # []
list5 = listToLinkedList([])
list6 = listToLinkedList([0])          # [0]

# 1. 책
# 재귀를 이용해 문제 품
# LinkedList의 갠며에 대한 이해가 더 필요할듯
def mergeTwoLists1(list1, list2):
    print('start')
    print('list1', printLinkedList(list1))
    print('list2', printLinkedList(list2))
    if (not list1) or (list2 and list1.val > list2.val):
        list1, list2 = list2, list1
    if list1:
        list1.next = mergeTwoLists1(list1.next, list2)
    return list1

printLinkedList(mergeTwoLists1(list1, list2))