"""
Problem
- Given lower case english words, anytime you see "aeiou", we remove it
- Relative order of string is kept

Strategy
- We could go thru each i of s, whenever we see "aeiou" we can perform a <- shift
- We can also just slice the string without that given index
- So given an i is a vowel we want 
    - Slice before s[:i], and then skip it   s[i+1:]

Cases
- Length 1, is a vowel, should return the empty string
    - What happens if you slice before and provide an index too large?
"""
class Solution:
    def removeVowels(self, s: str) -> str:
        res = s
        vowels = "aeiou"

        i = 0
        while i < len(res):
            c = res[i]
            if c in vowels:
                res = res[:i] + res[i+1:]
            else:
                i += 1
        
        return res
