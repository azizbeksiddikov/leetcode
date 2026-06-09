# Link: https://leetcode.com/problems/lru-cache

import json


class CacheNode:
    def __init__(self, key=None, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = {}  # key => node
        self.start = CacheNode()
        self.end = CacheNode()
        self.start.next = self.end
        self.end.prev = self.start

    def print_list(self):
        res = []
        curr = self.start
        while curr:
            res.append(curr.val)
            curr = curr.next
        print("arr:", res)
        print(json.dumps({k: node.val for k, node in self.store.items()}, indent=4))

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        node = self.store[key]

        node.prev.next = node.next
        node.next.prev = node.prev
        if self.end != node:
            self.end.prev.next = node
            node.prev = self.end.prev
            self.end.prev = node
            node.next = self.end
        self.print_list()
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            node = self.store[key]
            # remove from current position
            node.prev.next = node.next
            node.next.prev = node.prev

            node.val = value
        else:
            node = CacheNode(key, value)
            self.store[key] = node

        self.end.prev.next = node
        node.prev = self.end.prev
        self.end.prev = node
        node.next = self.end

        # delete if capacity exists
        if self.capacity < len(self.store):
            node_to_delete = self.start.next
            node_to_delete.next.prev = self.start
            self.start.next = node_to_delete.next

            del self.store[node_to_delete.key]
            del node_to_delete
        self.print_list()


# lRUCache = LRUCache(3)
# print("\n\n***** PART A *****\n\n")
# lRUCache.put(1, 1)
# lRUCache.put(2, 2)
# lRUCache.put(3, 3)
# print(lRUCache.get(1))
# print(lRUCache.get(2))
# print(lRUCache.get(4))
# lRUCache.put(4, 4)
# print("\n\n***** PART B *****\n\n")
# print(lRUCache.get(1))
# print(lRUCache.get(2))
# print(lRUCache.get(3))
# print(lRUCache.get(4))
# print(lRUCache.get(2))
# print("\n\n***** PART C *****\n\n")
# lRUCache.put(1, 8)
# lRUCache.put(3, 7)
# print("\n\n***** PART D *****\n\n")
# print(lRUCache.get(1))
# print(lRUCache.get(2))
# print(lRUCache.get(3))
# print(lRUCache.get(4))
# print(lRUCache.get(5))
# print(lRUCache.get(2))
# print(lRUCache.get(3))
# print(lRUCache.get(4))
# lRUCache.put(1, 9)
# lRUCache.put(6, 6)
# print(lRUCache.get(1))
# print(lRUCache.get(2))
# print(lRUCache.get(3))
# print(lRUCache.get(4))
# print(lRUCache.get(5))
# print(lRUCache.get(6))
