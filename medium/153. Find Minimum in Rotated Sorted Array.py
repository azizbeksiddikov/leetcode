# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

class Solution:
    def findMin(self, nums: list[int]) -> int:
        # divide arr in 2 subarrays
        # if no unsorted => return leftmost
        # if unsorted: go and search there
        res = nums[0]
        l, r = 0, len(nums) - 1
        
        while l <= r:
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break
            m = l + ((r - l) // 2)
            res = min(res, nums[m])
            # print(f"l: {l}=>{nums[l]}, m: {m}=>{nums[m]}, r: {r}=>{nums[r]}, res: {res}")
            
            # left side is sorted: go right
            if nums[l] <= nums[m]:
                l = m + 1
            # right side is sorted: go left
            elif nums[m] < nums[r]:
                r = m - 1
        return res


# rotations happens from left to right
# nums = [3,4,5,6,1,2] # 1
# nums = [4,5,0,1,2,3] # 0
# nums = [4,5,6,7] # 4
# print(Solution().findMin(nums))
