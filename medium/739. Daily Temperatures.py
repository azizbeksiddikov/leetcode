# Link: https://leetcode.com/problems/daily-temperatures

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        maxStack = [] # (temp, index)
        result = [0] * len(temperatures)
        
        for i, temperature in enumerate(temperatures):
            # print(f"temperature: {temperature}; stack top: {maxStack[-1] if maxStack else None}")
            while maxStack and temperature > maxStack[-1][1]:
                idx, ele = maxStack.pop()
                result[idx] = i - idx # get the distance
            maxStack.append((i, temperature))

        return result

# temperatures = [30,38,30,36,35,40,28] # [1,4,1,2,1,0,0]
# temperatures = [22,21,20] #[0,0,0]
# print(Solution().dailyTemperatures(temperatures))