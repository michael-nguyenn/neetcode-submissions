class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # make a prefix array counting number of words that start & end with a vowel
        prefix = []
        vowels = "aeiou"
        total_count = 0
        res = []

        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                total_count += 1
            prefix.append(total_count)
        
        # now we go through each query 
        # the number of valid strings will be the number of
        # valid words at end index - the valid words before the start index
        for start, end in queries:
            if start == 0:
                res.append(prefix[end])
            else:
                res.append(prefix[end] - prefix[start - 1])
        
        return res

        