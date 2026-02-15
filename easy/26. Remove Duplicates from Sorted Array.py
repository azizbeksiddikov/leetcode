# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        expected_arr = []

        for i in range(len(nums)):
            if not nums[i] in expected_arr:
                expected_arr.append(nums[i])
                nums[k] = nums[i]
                k += 1
                

        return k
