# Definition for singly-linked list.

from typing import Optional


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
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left, right = dummy, head

        for _ in range(n):
            right = right.next

        while right:
            left = left.next
            right = right.next

        # delete
        left.next = left.next.next
        return dummy.next


# test 1
head = [1, 2, 3, 4]
n = 2

# test 2
head = [5]
n = 1

# test 3
head = [1, 2]
n = 2

input = make_list(head)
s = Solution()
res_head = s.removeNthFromEnd(input, n)
print(read_list(res_head))
