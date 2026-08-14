class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        first, second = 0, 0
        res = ""

        while first < len(word1) and second < len(word2):
            res += f"{word1[first]}{word2[second]}"
            first += 1
            second += 1
        
        if first == len(word1):
            res += word2[second:]
        else:
            res += word1[first:]
            
        return res