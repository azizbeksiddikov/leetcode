# Link: https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = Counter(nums)

        sortedArray = sorted(countMap, key=lambda key: countMap[key], reverse=True)
        array = list(sortedArray)

        return array[0: k]
