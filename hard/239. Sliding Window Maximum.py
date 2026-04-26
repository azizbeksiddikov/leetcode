# Link: https://leetcode.com/problems/sliding-window-maximum
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res = []
        queue = deque()
        l = r = 0

        while r < len(nums):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)

            if l > queue[0]:
                queue.popleft()
            
            if (r + 1) >= k:
                res.append(nums[queue[0]])
                l += 1
            r += 1
        return res

# nums, k = [1,2,1,0,4,2,6], 3
# nums, k =[1,3,-1,-3,5,3,6,7], 3
# nums, k =[1, -1], 1
# print(Solution().maxSlidingWindow(nums, k))
# O(nlogn) time and O(n) space
# where n is the size of the input array.