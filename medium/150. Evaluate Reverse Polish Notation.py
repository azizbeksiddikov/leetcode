# Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        nums = []
        
        for ele in tokens:
            if ele in {"+", "-", "/", "*"}:
                num2, num1 = nums.pop(), nums.pop()
                if ele == "+":
                    nums.append(num1 + num2)
                elif ele == "-":
                    nums.append(num1 - num2)
                elif ele == "*":
                    nums.append(num1 * num2)
                else:
                    nums.append(int(num1/num2))
                # print(f"ele: {ele}, nums: {nums}")
            else:
                nums.append(int(ele))
                # print(f"ele: {ele}, nums: {nums}")
        return nums.pop()
    
        
# tokens=["1","2","+","3","*","4","-"]
# tokens=["4","-2","/","2","-3","-","-"]
# print(Solution().evalRPN(tokens))