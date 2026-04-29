class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to hold opening braces
        my_stack = []
        o_braces = ['[', '{', '(']
        c_braces = [']', '}', ')']

        # Loop through the string
        for i in range(len(s)):
            # If it is a closing bracket add it to our stack
            if s[i] in o_braces:
                my_stack.append(s[i])

            if s[i] in c_braces:
                # If our stack is empty at this point it means
                # we're missing the corresponding brace
                if not my_stack: return False

                # Otherwise we'll pop from the stack and compare
                open_brace = my_stack.pop()

                if s[i] == ']' and open_brace != '[': return False
                elif s[i] == '}' and open_brace != '{': return False
                elif s[i] == ')' and open_brace != '(': return False

        
        # Now we're out the loop, if there are any leftovers in the stack
        # it means there was no matching opening brace
        if my_stack: return False

        # Since we've made it here, it is good
        return True
        