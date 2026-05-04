class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        o_brackets = []

        for c in s:
            # opening bracket case
            if c == '(' or c == '{' or c == '[':
                o_brackets.append(c)
            # closing bracket case
            else:
                # empty or mismatch = non valid
                if len(o_brackets) == 0:
                    return False

                opening = o_brackets.pop()

                if brackets[c] != opening:
                    return False
        
        return len(o_brackets) == 0