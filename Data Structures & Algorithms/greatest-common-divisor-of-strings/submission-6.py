"""
Problem
t divides s if s = t+t+t... (t is appended to itself 1 or more times)
given two strings, find string x where it divides both str1 and str2

Example 
ABAB, AB
- AB divides both AB and ABAB
NANANA and NANA
- NANA divides NANANA and NANA

Strategy
- Get the length of the shorter string, and loop back from that length
- The shorter length represents the maximum size the divisor could be
- You check if that length can divide into both strings first via modulo
- Then you see how many times the divisor can fit into each string
- Afterwards you compare to see if the divisor * occurences match

Trace NANANA, NANA
First check len(4)
- It mods NANA ok but not NANANA so we return False
Then check 3
- Doesn't mod into either, False
Then check 2
- Mods into both
- Get the times it could fit into both, NANANA=3, NANA=2
- then we compare str1[:l]*occur1 == str2[:l]*occur2 so NA*3 == NA*2, it matches so we return

"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def can_divide(length):

            # You check if that length can divide into both strings first via modulo
            if len1 % length != 0 or len2 % length != 0:
                return False

            # Check if the prefix of both strings is identical
            if str1[:length] != str2[:length]:
                return False

            # see how many times the divisor can fit into each string
            times1 = len1 // length
            times2 = len2 // length

            # see if they are multiples of each other
            return str1[:length]*times1 == str1 and str2[:length]*times2 == str2
            
        for length in range(min(len1, len2), 0, -1):
            if can_divide(length):
                return str1[:length]
        
        return ""
        