# Link: https://leetcode.com/problems/longest-repeating-character-replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        maxFreq, res = 0, 0
        l = 0
        
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1

            maxFreq = max(maxFreq, freq[s[r]])
            while (r - l + 1) - maxFreq > k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
        
# s, k = "XYYX", 2 # 4
# s, k = "AAABABB", 1 # 5
# s, k ="AAAB", 0 # 3
# s, k ="ABAA", 0 # 2
# print(Solution().characterReplacement(s, k))