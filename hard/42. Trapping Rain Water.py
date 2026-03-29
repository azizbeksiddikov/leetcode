# Link: https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        res = 0
        max_heights = [0] * n
        
        # Find the left max
        l_max = 0
        for i, a in enumerate(height):
            if a > height[l_max]:
                l_max = i
            max_heights[i] = height[l_max]
        # print("after left max iterations:", max_heights)

        # Find the right max - reverser order
        r_max = n - 1
        for i in range(n - 1, -1, -1):
            if height[i] > height[r_max]:
                r_max = i
            max_heights[i] = min(max_heights[i], height[r_max])
        # print("after right max iterations:", max_heights)
        
        # Calculate the area
        for i, a in enumerate(height):
            res += max_heights[i] - a
            # print(f"{i} index: height={max_heights[i]}, water: {max_heights[i] - a}")
        return res
        
# height = [0,2,0,3,1,0,1,3,2,1]
# print("res:", Solution().trap(height))

