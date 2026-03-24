# Link: https://leetcode.com/problems/longest-consecutive-sequence

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        
        for i, num in enumerate(nums_set):
            if (num - 1)in nums_set:
                continue
            
            curr_len = 1
            while (num + 1) in nums_set:
                curr_len += 1
                num += 1
            if curr_len > max_len:
                max_len = curr_len
        return max_len


# nums = [2,20,4,10,3,4,5]
nums = [0,3,2,5,4,6,1,1]

print(Solution().longestConsecutive(nums))
