from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque()
        visited = set()

        q.append((beginWord, 1)) # word and path length
        visited.add(beginWord)

        while q:
            word, path_len = q.popleft()

            if word == endWord:
                return path_len

            for w in wordList:
                if w in visited:
                    continue
                
                if not self.differs_by_one(word, w):
                    continue
                
                # otherwise load up the q
                visited.add(w)
                q.append((w, path_len + 1))
        
        return 0 # this means there is no valid


    def differs_by_one(self, word1: str, word2: str) -> bool:
        diff = 0

        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                diff += 1
        
        return diff == 1