"""
Problem
- Each number 2-9 represents a set of alphabet chars
- We're given a string of digits, and we must include all combos aka cross products of the numbers

Example 234
- adg, adh, adi, aeg, aeh, aei, afg, afh, afi
- bdg, bdh, bdi, beg, beh, bei, bfg, bfh, bfi
- cdg, cdh, cdi, ceg, ceh, cei, cfg, cfh, cfi

Strat
- We first need to create a mapping of digits to characters: 2 -> [a, b, c]
- backtrack over possible permutations
- pass in the index of the num string
- get the mapping [a, b, c]
- For each letter in the mapping
    - Add it to the path
    - Call backtrack on the next index
    - Remove it from path

Base Case
- If we reach past the end of digits, so len(digits) == i 
    - Then we want to create a copy of the path, and return
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        path = []
        res = []

        def backtrack(i:int) -> None:
            if i == len(digits):
                res.append("".join(path))
                return
            
            chars = mapping[digits[i]]

            for char in chars:
                path.append(char)
                backtrack(i+1)
                path.pop()
            
        backtrack(0)
        return res
        