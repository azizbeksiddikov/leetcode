# Link: https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = "".join(char.lower() for char in s if char.isalnum())
        
        
        start = 0
        end = -1
        
        for i in range(len(new_s)):
            if new_s[start] != new_s[end]:
                return False
            start += 1
            end -= 1
        
        return True
    
# s = "Was it a car or a cat I saw?"
s = "race a car"
print(Solution().isPalindrome(s))