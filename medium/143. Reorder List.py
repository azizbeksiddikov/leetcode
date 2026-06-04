# Link: https://leetcode.com/problems/reorder-list
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
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # 1. Find the middle node
        # Move fast pointer 2 steps, slow pointer 1 step
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head_2 = slow.next
        slow.next = None

        # 2. Reorder the second half
        curr = head_2
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # 3. Reorder into the final version
        curr_1, curr_2 = head, prev
        while curr_1 and curr_2:
            temp1 = curr_1.next
            temp2 = curr_2.next
            curr_1.next = curr_2
            curr_2.next = temp1
            curr_1 = temp1
            curr_2 = temp2


arr = [2, 4, 6, 8, 10]
# arr = [2, 4, 6, 8]
s = Solution()
nums = make_list(arr)
s.reorderList(nums)
print(read_list(nums))
# print(read_list(res[1]))
