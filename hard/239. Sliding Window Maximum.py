# Link: https://leetcode.com/problems/sliding-window-maximum

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res = []
        queue = []

        for i in range(len(nums) - k + 1):
            print(f"start: {nums[i : i + k]}, queue: {queue}, res: {res}")
            
            # first built-up
            if i == 0:
                for idx in range(k):
                    while queue and nums[queue[-1]] < nums[idx]:
                        queue.pop()
                    queue.append(idx)
            else:
                newNumberIndex = i + k - 1
                
                while queue and nums[queue[-1]] < nums[newNumberIndex]:
                    queue.pop()
                queue.append(newNumberIndex)

                if queue and queue[0] < i:
                    del queue[0]
            
            res.append(nums[queue[0]])
            print(f"after: {nums[i : i + k]}, queue: {queue}, res: {res}\n")
        return res

# nums, k = [1,2,1,0,4,2,6], 3
# nums, k =[1,3,-1,-3,5,3,6,7], 3
# nums, k =[1, -1], 1
# print(Solution().maxSlidingWindow(nums, k))
# O(nlogn) time and O(n) space
# where n is the size of the input array.