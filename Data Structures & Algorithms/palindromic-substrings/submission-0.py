class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def expand_middle(left: int, right:int):
            nonlocal res;

            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        
        for i in range(len(s)):
            expand_middle(i, i)
            expand_middle(i, i+1)

        return res