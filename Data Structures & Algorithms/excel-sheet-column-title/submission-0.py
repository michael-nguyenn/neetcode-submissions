"""
Problem
- Given a column number, and we need to figure out corresponding title

Example A
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []

        while columnNumber > 0:
            columnNumber -= 1 # adjust for 0 offset
            offset = columnNumber % 26
            res.append(chr(ord('A') + offset))
            columnNumber //= 26
        
        return "".join(reversed(res))
        