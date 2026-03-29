# Link: https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        total_water = 0
        
        while l < r:
            # print(f"Compare: l={l} {height[l]}; r={r} {height[r]}; l_max={l_max}, r_max={r_max}")
            if l_max <= r_max:
                l += 1
                l_max = max(l_max, height[l])
                total_water += l_max - height[l]
            else:
                r -= 1
                r_max = max(r_max, height[r])
                total_water += r_max - height[r]
            # print(f"total_water: {total_water}")
        return total_water
        
# height = [0,2,0,3,1,0,1,3,2,1]
# print("total_water:", Solution().trap(height))
