class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}

        for char in s:
            if char in d1:
                d1[char] += 1
            else:
                d1.setdefault(char, 1)

        for c in t:
            d2[c] = d2.get(c, 0) + 1

        return d1 == d2
        