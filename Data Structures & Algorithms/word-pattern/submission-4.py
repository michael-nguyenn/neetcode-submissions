class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping = {}
        seen = set()
        words = s.split(' ')

        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            if pattern[i] in mapping:
                if i >= len(words) or words[i] != mapping[pattern[i]]:
                    return False
            else:
                if i >= len(words) or words[i] in seen:
                    return False
                
                mapping[pattern[i]] = words[i]
                seen.add(words[i])

        return True