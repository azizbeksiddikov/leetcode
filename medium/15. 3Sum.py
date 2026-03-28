# Link: https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if (i > 0 and a == nums[i-1]) or a > 0:
                continue
        
            l, r = i + 1, len(nums)-1
            while l < r:
                # print(f"i={i}:{nums[i]}; l={l}:{nums[l]}; r={r}:{nums[r]}; SUM: {a + nums[l] + nums[r]}")
                sum = a + nums[l] + nums[r]
                if sum == 0:
                    res.append([a, nums[l], nums[r]])    
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1
        return res
        

# nums = [-1,0,1,2,-1,-4]
# nums = [0,1,1]
# nums = [0, 0, 0]
# nums = [-2,0,0,2,2]
# nums = [-4,-2,-1]
# print("res:", Solution().threeSum(nums))

