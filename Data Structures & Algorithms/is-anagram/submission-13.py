class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        counts = {}

        for i in range(len(s)):
            counts[s[i]] = 1 + counts.get(s[i], 0)
            counts[t[i]] = counts.get(t[i], 0) - 1

        for value in counts.values():
            if value != 0:
                return False

        return True
        