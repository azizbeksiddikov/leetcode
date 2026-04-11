# Link: https://leetcode.com/problems/median-of-two-sorted-arrays

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        # A is a smaller array
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
          
        l, r = 0, len(A) - 1
        while True:
            i = (r + l) // 2 # A
            j = half - i - 2 # B
            
            Aleft = A[i] if i >= 0 else float("-infinity") 
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity") 
            Bleft = B[j] if j >= 0 else float("-infinity") 
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity") 
            
            # print(f"l={l}, r={r}, i={i}, j={j}, Aleft={Aleft}, Aright={Aright}, Bleft={Bleft}, Bright={Bright}")
            
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
        

# nums1, nums2 = [1,2], [3]   # 2.0
# nums1, nums2 = [1,3], [2,4] # 2.5
# nums1, nums2 = [], [1]
# nums1, nums2 = [2], []
# print("findMedianSortedArrays:", Solution().findMedianSortedArrays(nums1, nums2))
# O(log(m+n)) time.
