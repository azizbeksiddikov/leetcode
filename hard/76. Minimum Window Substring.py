# Link: https://leetcode.com/problems/minimum-window-substring

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        left and right pointers

        update rigth: when conditions are not satified
        update left:  when conditions are satified

        confitions are satisfied when windowMap contains targetMap
        """
        l, r = 0, len(t) - 1
        res = ""
        if len(s) < len(t):
            return res
        
        # Build the target dict
        targetMap = {}
        for ch in t:
            targetMap[ch] = targetMap.get(ch, 0) + 1
        # print("targetMap", targetMap)

        # Build the window dict
        windowDict = {}
        for ch in s[l:r + 1]:
            windowDict[ch] = windowDict.get(ch, 0) + 1

        while r < len(s):
            # print(f"\ncurrent_window: '{s[l:r + 1]}', windowDict: {windowDict}")

            # Check validitity of the window
            isValid = True
            for ch, count in targetMap.items():
                if windowDict.get(ch, 0) < count:
                    isValid = False
                    break
            # print(f"windowDict: {windowDict}, isValid: {isValid}")

            if isValid:
                if res:
                    res = s[l: r + 1] if (r - l + 1) < len(res) else res
                else:
                    res = s[l: r + 1]
                # print(f"res: '{res}'")
                windowDict[s[l]] -= 1
                l += 1
            else:
                r += 1
                if r < len(s):
                    windowDict[s[r]] =  windowDict.get(s[r], 0) + 1
        return res


# s, t = "OUZODYXAZV", "XYZ"   # "YXAZ"
# s, t = "x", "xy"             # ""
s, t = "ADOBECODEBANC", "ABC" # "BANC"
print(Solution().minWindow(s, t)) 

# O(len(s)) time
# O(number of unique characters in s and t) space
