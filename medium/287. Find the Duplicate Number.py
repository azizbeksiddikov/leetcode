# Link: https://leetcode.com/problems/find-the-duplicate-number

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        # find an intersection
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # find the slow pointer
        slow2 = 0
        while True:
            slow2 = nums[slow]
            slow = nums[slow]
            if slow == slow2:
                return slow


# nums = [1, 2, 3, 2, 2]  # 2
# nums = [1, 2, 3, 4, 4]  # 4

# s = Solution()
# print(s.findDuplicate(nums))
