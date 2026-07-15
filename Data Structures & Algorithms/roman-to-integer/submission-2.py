class Solution:
    def romanToInt(self, s: str) -> int:
        rMap = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        s = s.replace("IV", "IIII")
        s = s.replace("IX", "IIIIIIIII")
        s = s.replace("XL", "XXXX")
        s = s.replace("XC", "XXXXXXXXX")
        s = s.replace("CD", "CCCC")
        s = s.replace("CM", "CCCCCCCCC")
        # print(s)
        res = 0

        for l in s:
            res += rMap[l]

        return res