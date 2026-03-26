# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        start_index = 0
        end_index = len(numbers) - 1
        
        print(start_index, end_index)
        while True:
            if start_index >= end_index:
                return False
            
            curr_sum = numbers[start_index] + numbers[end_index]
            if curr_sum == target:
                return [start_index+1, end_index+1]
            elif curr_sum > target:
                end_index -= 1
            else: 
                start_index += 1

# numbers = [1,2,3,4]
# target = 3
# print("result:", Solution().twoSum(numbers, target))
