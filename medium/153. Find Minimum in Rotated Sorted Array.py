# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            m = l + ((r - l) // 2)
            
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]
    
# rotations happens from left to right
# nums = [3,4,5,6,1,2] # 1
# nums = [4,5,0,1,2,3] # 0
# nums = [4,5,6,7] # 4
# print(Solution().findMin(nums))
