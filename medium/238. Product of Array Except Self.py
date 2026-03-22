# Link: https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix_arr: list[int] = []
        postfix_arr = [1] * len(nums)
        result = [1] * len(nums)
        
        # original:[1,  2,   4, 6]
        # prefix:  [1,  1,   2, 8]
        # postfix: [48, 24,  6, 1]
        # result:  [48, 24, 12, 8]
        
        print("nums", nums)
        
        # start => end: prefix arr
        for idx, num in enumerate(nums):
            # print(idx, num)
            if idx == 0:
                prefix_arr.append(1)
                continue
            prefix_arr.append(prefix_arr[idx-1] * nums[idx-1])
        print("prefix arr", prefix_arr)
        
        # end => start: postfix arr
        for idx in range(len(nums)-1, -1, -1):
            if idx == len(nums)-1:
                postfix_arr[idx] = 1
                continue
            postfix_arr[idx] = nums[idx+1] * postfix_arr[idx+1]
        print("postfix_arr", postfix_arr)
        
        result = [postfix_arr[idx] * prefix_arr[idx] for idx in range(len(nums))]
        return result



# nums = [1,2,4,6]
# result = Solution().productExceptSelf(nums)
# print("result", result)