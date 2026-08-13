class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # If there is only one word it's auto valid
        if len(words) == 1:
            return True

        # Pre compute the ordering of their alphabet O(n)
        mapping = {}

        rank = 0
        for char in order:
            mapping[char] = rank
            rank += 1
        
        # Go through each pair of words and find the first non matching
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            if len(w2) < len(w1) and w1.startswith(w2):
                return False
            
            j = 0
            while j < len(w1) and w1[j] == w2[j]:
                j += 1

            if j == len(w1):
                continue
            elif mapping[w1[j]] < mapping[w2[j]]:
                continue
            else:
                return False
        
        return True
            