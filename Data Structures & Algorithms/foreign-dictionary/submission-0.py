class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        res = []

        visited = {} # false = visited ; true = visited + in cur path

        # adj represents a c -> char it comes before
        adj = {c:set() for w in words for c in w}

        # to build our list we want to go through each pair of words
        # and then compare until we find a differing char
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]

            # if we compare up to min_len, then the first word is a prefix of the second
            min_len = min(len(w1), len(w2))

            # edge case: if w1 is longer and contains the same prefix it's in invalid ordering
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            # now we can loop through both words, and upon finding a differing char
            # then we know that char comes before the other char in w2
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        def dfs(c) -> bool:
            # true means we've detected a loop
            if c in visited:
                return visited[c]

            visited[c] = True

            # go thru neighbors and dfs
            for neigh in adj[c]:
                if dfs(neigh):
                    return True
            
            visited[c] = False # afterwards we'll leave it marked, but allow others to visit
            res.append(c) # we add chars in post order
        

        # now for the main loop we go through each char in the adj list
        for c in adj:
            if dfs(c):
                return ""
        
        # at the end we reverse and return that string
        res.reverse()
        return "".join(res)

        
