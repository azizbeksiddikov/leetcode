# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, res= 0, 0, 0

        mySet = set()
        while r < len(s):
            # print("before:", l,r,mySet)
            if s[r] not in mySet:
                mySet.add(s[r])
            else:
                res = max(res, r - l)
                # update l until unqiue set
                while s[l] != s[r]:
                    l += 1
                l += 1 
                mySet = {ele for ele in s[l:r+1]}
            r += 1
            # print("after: ", l,r,mySet, "\n")

        return max(res, r - l)
        
# s = "zxyzxyz" # 3
# s = "bbbbb" # 1
# s = "pwwkew"
# s=" "
# s="dvdf"

print(Solution().lengthOfLongestSubstring(s))