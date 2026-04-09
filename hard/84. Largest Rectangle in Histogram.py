# Link: https://leetcode.com/problems/largest-rectangle-in-histogram

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxArea = 0
        stack = [] # (index, height)
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i -  index))
                start = index
            stack.append((start, h))

        n = len(heights)
        for i, h in stack:
            maxArea = max(maxArea, h * (n -  i))
        
        return maxArea

# heights = [7,1,7,2,2,4] # 8
# print("largestRectangleArea:", Solution().largestRectangleArea(heights))
