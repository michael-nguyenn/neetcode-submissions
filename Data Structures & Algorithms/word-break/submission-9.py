class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        dp[len(s)] = True

        for i in range(len(s) -1, -1, -1):
            print(s[i])
            for w in wordDict:
                if i+len(w) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i + len(w)]
                else:
                    dp[i] = False
                    
                if dp[i]:
                    break
        
        return dp[0]
        