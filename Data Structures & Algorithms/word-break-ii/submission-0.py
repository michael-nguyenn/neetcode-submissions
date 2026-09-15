class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        path, res = [], []

        def dfs(i):
            if i == len(s):
                res.append(" ".join(path))
                return
            
            for word in wordDict:
                n = len(word)

                if i + n <= len(s) and s[i:i+n] == word:
                    path.append(word)
                    dfs(i + n)
                    path.pop()
            
        dfs(0)
        return res
        