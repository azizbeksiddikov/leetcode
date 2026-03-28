# Link: https://leetcode.com/problems/container-with-most-water

class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        l, r = 0, len(height) - 1
        
        while l < r:
            area = (r - l) * min(height[l], height[r])
            if area > max_area:
                max_area = area
            
            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1
        
        return max_area

# height = [1,7,2,5,4,7,3,6]
# print("res:", Solution().maxArea(height))
