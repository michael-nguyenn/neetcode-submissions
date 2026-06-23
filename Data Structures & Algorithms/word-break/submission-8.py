class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = { len(s): True }

        def dfs(i):
            if i in memo:
                return memo[i]
            
            for w in wordDict:
                # we will only make the next dfs call if we can actually
                # match word w to s[i + len(w)]
                
                # have to make sure we can even slice that far
                if i+len(w) > len(s):
                    continue

                # now we can recurse and repeat for the next word in s
                if s[i:i+len(w)] == w:
                    if dfs(i + len(w)):
                        memo[i] = True 
                        return True
            
            # if we ever go thru all the words in s then we're donezo
            memo[i] = False
            return False
        
        return dfs(0)
                
            