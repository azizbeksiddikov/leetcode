# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = ""
        maxLen = 0

        for char in s:
            if char in seen:
                while char in seen:
                    seen = seen[1:]
            seen += char
            maxLen = max(maxLen, len(seen))
        return maxLen
        
# s = "zxyzxyz" # 3
# s = "bbbbb" # 1
# s = "pwwkew"
# s=" "
# s="dvdf"
# print(Solution().lengthOfLongestSubstring(s))