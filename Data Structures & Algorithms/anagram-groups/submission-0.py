from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = defaultdict(list)

        for word in strs:
            key = tuple(sorted(word))
            counts[key].append(word)

        return list(counts.values())

        