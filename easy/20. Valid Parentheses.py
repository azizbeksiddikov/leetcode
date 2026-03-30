# Link: https://leetcode.com/problems/valid-parentheses


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par_dict = {")": "(", "}": "{", "]": "["}

        for i, ele in enumerate(s):
            if ele in par_dict:
                if len(stack) == 0:
                    return False
                matching_ele = par_dict[ele]
                if stack.pop() != matching_ele:
                    return False
            else:
                stack.append(ele)

        if len(stack) != 0:
            return False
        return True


s = "([{}])"
s = "[]"
s = "[(])"
s = "(){}}{"
print(Solution().isValid(s))
