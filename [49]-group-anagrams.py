from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = defaultdict(list)

        for word in strs:
            key = tuple(sorted(word))
            anagramDict[key].append(word)

        return list(anagramDict.values())