# Link: https://leetcode.com/problems/koko-eating-bananas

import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        
        # for each speed, calculate the hours
        # if hours can be satisfied, decrease speed
        # if hours exceeds minimmum, increase speed
        minSpeed, maxSpeed = 0, max(piles)
        
        l_speed, r_speed = 1, maxSpeed 
        while l_speed <= r_speed:
            curr_hours = 0
            speed = l_speed + ((r_speed - l_speed) // 2)
            # print(f"minSpeed:{minSpeed} => l_speed:{l_speed} => speed:{speed} => r_speed:{r_speed}, maxSpeed:{maxSpeed}")
            
            # Calculate hours for given speed
            for banana in piles:
                curr_hours += math.ceil(banana / speed)
            # print(f"curr_hours: {curr_hours}, target: {h}, satisfies: {True if curr_hours <= h else False}")
            
            if curr_hours <= h:
                maxSpeed = speed
                r_speed = speed - 1
                # print(f"(after) minSpeed:{minSpeed} => l_speed:{l_speed} => r_speed:{r_speed}, maxSpeed:{maxSpeed}\n")
                if r_speed <= minSpeed:
                    return maxSpeed
            else:
                minSpeed = speed
                l_speed = speed + 1
                # print(f"(after) minSpeed:{minSpeed} => l_speed:{l_speed} => r_speed:{r_speed}, maxSpeed:{maxSpeed}\n")
                if l_speed >= maxSpeed:
                    return maxSpeed
        
    
# piles = [1,4,3,2]
# h = 9 # output: 2

# piles=[3,6,7,11]
# h=8 # output: 4, my-3

# piles=[312884470]
# h=968709470
# print(Solution().minEatingSpeed(piles, h))