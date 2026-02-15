# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        dict_res = {}

        for i in range(len(nums)):
            if not nums[i] in dict_res:
                dict_res[nums[i]] = False
                nums[k] = nums[i]
                k += 1
            elif dict_res[nums[i]] == False:
                dict_res[nums[i]] = True
                nums[k] = nums[i]
                k += 1
        return k
