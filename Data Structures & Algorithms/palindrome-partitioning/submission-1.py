"""
Problem
- Given a string, must split into substrings where all substrings are palindromes
- smallest palindrome is a single char
- 

Strategy
- base case is when i == len(s), return the copied cur
- starting at an index i, if adding this char is a valid palindrome, then we create the string, and call backtrack(i+1)

Example 
"acab"
- a c a b, aca b

"caaa"
- c a a a, base case [c a a a]
- [c a a], can make c a aa 
- [c a] can make c aa, c aa a 
- [c aaa]

"efe"
backtrack(0)
- cur_s = ""
- cur_s = "e", cur = [e]
    backtrack(1)
    - cur_s = ""
    - cur_s = "f", cur = [e f]
        backtrack(2)
        - cur_s = ""
        - cur_s = "e", append cur = [e f e]
            backtrack(3)
            - base case returns
        - pop from cur = [e f]
        - returns
    - pops from cur [e]
    - is_palindrome(1, 2) "fe" = False
    - returns
- pop from cur [], cur_s = "e"
- is_palindeome(0, 1) "ef" = False
- is_palindrome(0, 2) "efe" = True
- cur_s = "efe", append cur = [efe]
    backtrack(3)
"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []
        
        # correct fosho
        def is_palindrome(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        def backtrack(start):
            if start == len(s):
                res.append(cur.copy())
                return
            
            for i in range(start, len(s)):
                if is_palindrome(start, i):
                    cur.append(s[start:i+1])
                    backtrack(i+1)
                    cur.pop()
        
        backtrack(0)
        return res



    
        