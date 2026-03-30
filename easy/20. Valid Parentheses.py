# Link: https://leetcode.com/problems/valid-parentheses


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {")": "(", "]": "[", "}": "{"}

        for ele in s:
            if ele in close_to_open:
                if len(stack) == 0 or stack.pop() != close_to_open[ele]:
                    return False
            else:
                stack.append(ele)

        return True if not stack else False


# s = "([{}])"
# s = "[]"
# s = "[(])"
# s = "(){}}{"
# print(Solution().isValid(s))
