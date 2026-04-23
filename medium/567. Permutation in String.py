# Link: https://leetcode.com/problems/permutation-in-string
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        # map chars => counts for s1
        s1_map = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        for ele in s1:
            s1_map[ele] = s1_map.get(ele, 0) + 1
        # print(s1_map)

        # get the dict of sliding window of s2
        target_map = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        for i in range(len(s2) - n + 1):
            # build dict first
            if i == 0:
                for ele in s2[i: i + n]:
                    target_map[ele] = target_map.get(ele, 0) + 1
            # add and delete only 1 ele in dict
            else:
                target_map[s2[i - 1]] -= 1
                target_map[s2[i + n - 1]] += 1

            if target_map == s1_map:
                return True
        return False

# s1, s2 = "abc", "lecabee" # true
# s1, s2 = "abc", "lecaabee" # false
# s1, s2 = "ab", "lecabee" # true
# print(Solution().checkInclusion(s1, s2))
