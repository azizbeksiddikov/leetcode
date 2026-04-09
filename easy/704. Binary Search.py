# Link: https://leetcode.com/problems/binary-search

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        middle = n // 2
        
        while right >= left:
            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
            middle = (left + right) // 2
    
        return -1

nums = [-1,0,2,4,6,8]
target = 4 
print(Solution().search(nums, target))
        
