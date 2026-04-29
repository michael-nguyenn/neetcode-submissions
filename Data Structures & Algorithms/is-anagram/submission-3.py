class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False

        s_counts = {}
        t_counts = {}

        for char in s:
            if char not in s_counts:
                s_counts[char] = 1
            else:
                s_counts[char] += 1

        for char in t:
            if char not in t_counts:
                t_counts[char] = 1
            else:
                t_counts[char] += 1

        return s_counts == t_counts

        