# Link: https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # how much is req : index of other value

        for i in range(len(nums)):
            curr_value = nums[i]
            required = target - curr_value

            if required in seen:
                return [seen[required], i]    
            else:
                seen[curr_value] = i
