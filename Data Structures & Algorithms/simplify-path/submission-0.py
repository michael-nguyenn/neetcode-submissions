"""
Problem
- given absolute path need to convert into simplified canonical path

Strategy
- the different types of strings we can run across
    - always begins with /
    - things inbetween two slashes are directories
    - . means current directory
    - .. means previous directory
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []

        for part in path:
            if part == "" or part == ".":
                continue
            elif part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        
        return "/" + "/".join(stack)

        