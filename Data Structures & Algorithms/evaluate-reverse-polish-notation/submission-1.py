class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = "+-*/"
        stack = []

        for token in tokens:
            
            if token not in operators:
                stack.append(token)
            else:
                op2 = int(stack.pop())
                op1 = int(stack.pop())

                if token == "+":
                    stack.append(op1 + op2)
                elif token == "-":
                    stack.append(op1 - op2)
                elif token == "*":
                    stack.append(op1 * op2)
                else:
                    stack.append(op1 / op2)
        
        return int(stack.pop())
            
        