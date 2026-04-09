# Link: https://leetcode.com/problems/largest-rectangle-in-histogram

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # stack - preserved heights
        n = len(heights)
        stack = [] # (index, value)
        max_area = 0
        
        for idx, height in enumerate(heights):
            # print(f"idx:{idx} | before: height:{height} max_area:{max_area} stack: {stack}")

            # compare with the latest stack elements
            # if desc: remove the larger ones, add to the stack
            # if same: continue
            # if asc: add to the stack
            if stack and stack[-1][1] > height:
                last_index = -1
                while stack and stack[-1][1] > height:
                    last_index, last_ele = stack.pop()
                    area = (idx -  last_index) * last_ele
                    if area > max_area:
                        max_area = area
                stack.append((last_index, height))
            elif stack and stack[-1][1] == height:
                pass
            else:
                stack.append((idx, height))

            # print(f"idx:{idx} | after:  height:{height} max_area:{max_area} stack: {stack}\n")
        
        while stack:
            last_index, last_ele = stack.pop()
            area = (n -  last_index) * last_ele
            if area > max_area:
                max_area = area
        
        return max_area

heights = [7,1,7,2,2,4] # 8
# stack:[ (0, 1)]
# curr ele: 7
# max_area: 7

# heights = [1,3,7] # 7
print("largestRectangleArea:", Solution().largestRectangleArea(heights))
