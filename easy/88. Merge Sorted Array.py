# Link: https://leetcode.com/problems/merge-sorted-array/description/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        idx, i, j = m+n-1, m-1, n-1

        while j >= 0:

            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[idx] = nums1[i]
                i -= 1
            else:
                nums1[idx] = nums2[j]
                j -= 1
            
            idx -= 1
