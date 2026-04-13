# Link: https://leetcode.com/problems/longest-repeating-character-replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        l, r = 0, 0
        
        def countDict(dict):
            # return (all - mostFreq char count)
            array = [dict[ele] for ele in dict]
            if not array:
                return 0
            return sum(array) - max(array)
         
        charDict = {}
        while r < len(s):
            # print("before:", l, r, maxLength, charDict, countDict(charDict))
            
            charDict[s[r]] = charDict.get(s[r], 0) + 1
            while countDict(charDict) > k:
                charDict[s[l]] -= 1
                l += 1
            maxLength = max(maxLength, (r - l + 1))
            
            # print("after: ", l, r, maxLength, charDict, countDict(charDict), "\n")
            r += 1

        return maxLength
        
# s, k = "XYYX", 2 # 4
# s, k = "AAABABB", 1 # 5
# s, k ="AAAB", 0 # 3
# s, k ="ABAA", 0 # 2
# print(Solution().characterReplacement(s, k))