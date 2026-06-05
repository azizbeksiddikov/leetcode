# Link: https://leetcode.com/problems/add-two-numbers

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def make_list(arr):
    temp = ListNode()
    curr = temp
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return temp.next


def print_list(head):
    arr = []
    curr = head
    while curr:
        arr.append(curr.val)
        curr = curr.next
    return arr


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode(0)
        curr = head

        additional = 0
        a, b = l1, l2
        while a and b:
            # print(f"a:{a.val}, b:{b.val}")
            summa = a.val + b.val + additional
            curr.next = ListNode(summa % 10)
            additional = summa // 10

            a = a.next
            b = b.next
            curr = curr.next

        while a:
            summa = a.val + additional
            curr.next = ListNode(summa % 10)
            additional = summa // 10
            a = a.next
            curr = curr.next

        while b:
            summa = b.val + additional
            curr.next = ListNode(summa % 10)
            additional = summa // 10
            b = b.next
            curr = curr.next

        if additional > 0:
            curr.next = ListNode(additional)

        return head.next


# l1 = [1, 2, 3]  # 321
# l2 = [4, 5, 6]  # 654
# Output: [5,7,9] # 975

# l1 = [9]
# l2 = [9]

# list1 = make_list(l1)
# list2 = make_list(l2)

# s = Solution()
# res = s.addTwoNumbers(list1, list2)
# print(print_list(res))
