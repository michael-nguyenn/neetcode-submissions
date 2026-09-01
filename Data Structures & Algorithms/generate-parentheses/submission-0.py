class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        res = []

        def dfs(left: int, right: int):
            if left == 0 and right == 0:
                res.append("".join(path))
                return
            
            if left < 0 or left > right:
                return
            
            # Otherwise we'll append the open brace, explore those paths
            path.append('(')
            new_left = left - 1
            dfs(new_left, right)
            path.pop()

            # once we're done that path we pop and explore if we hadn't added
            path.append(')')
            new_right = right - 1
            dfs(left, new_right)
            path.pop()
        
        dfs(n, n)
        return res