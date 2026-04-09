# Link: https://leetcode.com/problems/search-in-rotated-sorted-array

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        # find which subarray is sorted
        # if the ele in the sorted subarray: go more to that side
        # if the ele is not in the sorted subarray: go to the unsroted array
        
        while l <= r:
            m = l + ((r - l) // 2)
            if target == nums[m]:
                return m
            
            # left subarray is sorted
            if nums[l] <= nums[m]:
                # if ele in subarray
                if target >= nums[l] and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
                    
            # right subarray is sorted
            else:
                # if ele in subarray
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1


# nums = [3,4,5,6,1,2]
# target = 1 # 4
# nums = [3,5,6,0,1,2]
# target = 4 # -1
# nums=[4,5,6,7,0,1,2]
# target=0
# print("search:", Solution().search(nums, target))
