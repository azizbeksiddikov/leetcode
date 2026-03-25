# Link: https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = "".join(char.lower() for char in s if char.isalnum())
        return new_s==new_s[::-1] 
        
    
# s = "Was it a car or a cat I saw?"
s = "race a car"
print(Solution().isPalindrome(s))