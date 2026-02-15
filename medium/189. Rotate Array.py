# Link: https://leetcode.com/problems/rotate-array/description/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        arr = nums[-1 * k:] + nums[0:-1*k]
        for i in range(len(nums)):
            nums[i] = arr[i]
