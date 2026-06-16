class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_idx = 0
        res_len = 0

        def expand_from_center(l: int, r: int):
            nonlocal res_idx, res_len

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res_idx = l
                    res_len = r - l + 1
                l -= 1
                r += 1
        
        for i in range(len(s)):
            expand_from_center(i, i) # odd lengths
            expand_from_center(i, i + 1) # even lengths

        return s[res_idx : res_idx + res_len]