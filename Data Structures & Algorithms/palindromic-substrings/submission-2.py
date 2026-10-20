"""
Strategy
- Use two pointers to find the palindrome from the middle. You can go through each character in input s and attempt to expand outwards. We can keep expanding so long the characters at the pointers match up
- If we start our pointers on the same character they'll count odd length palindromes -> 1,3 5...
- If we start our pointers one apart they'll count even length ones
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.get_palindromes(i,i, s)
            res += self.get_palindromes(i,i+1, s)
        return res

    def get_palindromes(self, left, right, s):
        res = 0

        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            
            left -= 1
            right += 1
            res += 1
        
        return res


        