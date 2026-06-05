# Link: https://leetcode.com/problems/copy-list-with-random-pointer

from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


def make_list(arr):
    if not arr:
        return None

    nodes = [Node(val) for val, _ in arr]

    for i, (_, rand_idx) in enumerate(arr):
        # build next
        if i < len(nodes) - 1:
            nodes[i].next = nodes[i + 1]

        # build random
        if rand_idx is not None:
            nodes[i].random = nodes[rand_idx]
    return nodes[0]


def print_list(head):
    result = []
    curr = head
    while curr:
        rand_val = curr.random.val if curr.random else None
        result.append((curr.val, rand_val))
        curr = curr.next
    return result


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        orig_to_copy = {}

        # first iteration - create all copy nodes
        orig = head
        while orig:
            orig_to_copy[orig] = Node(orig.val)
            orig = orig.next

        # second iteration - attach next and random
        orig = head
        while orig:
            if orig.next:
                orig_to_copy[orig].next = orig_to_copy[orig.next]
            if orig.random is not None:
                orig_to_copy[orig].random = orig_to_copy[orig.random]
            orig = orig.next

        return orig_to_copy[head]


arr = [[3, None], [7, 3], [4, 0], [5, 1]]
head = make_list(arr)
s = Solution()
copy = s.copyRandomList(head)
print("Original:", print_list(head))
print("Copy:    ", print_list(copy))
