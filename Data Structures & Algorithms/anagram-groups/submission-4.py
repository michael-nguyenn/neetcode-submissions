from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = defaultdict(list)

        for word in strs:
            key = [0] * 26

            # inner loop is bounded by the length of the word
            for char in word:
                key[(ord(char) - ord('a'))] += 1
            
            # then we'll append the key and the original word
            counts[tuple(key)].append(word)
        

        return list(counts.values())


