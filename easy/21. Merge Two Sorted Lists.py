# Link: https://leetcode.com/problems/merge-two-sorted-lists

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def make_list(arr):
    dummy = ListNode()
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def read_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            
        # Handle remaining elements
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next


# s = Solution()
# list1 = make_list([1,2,4])
# list2 = make_list([1,3,5])
# print(read_list(s.mergeTwoLists(list1, list2)))  # [1, 1, 2, 3, 4, 5]

# list1 = make_list([])
# list2 = make_list([1, 2])
# print(read_list(s.mergeTwoLists(list1, list2)))  # [1, 2]

# list1 = make_list([])
# list2 = make_list([])
# print(read_list(s.mergeTwoLists(list1, list2)))  # []