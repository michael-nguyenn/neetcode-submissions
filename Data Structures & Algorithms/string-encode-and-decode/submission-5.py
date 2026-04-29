class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: return chr(257)

        lengths = []
        encoded_str = ""
        # calculate the lengths of all the strings
        for word in strs:
            lengths.append(len(word))

        # then start forming the encoded string
        for length in lengths:
            encoded_str += str(length) + ","
        encoded_str += "#"

        # then append all the words
        for word in strs:
            encoded_str += word
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        if s == chr(257): return []

        i = 0
        lengths, res = [], []
        # extract the lengths from begin until #
        curr_len = ""
        while s[i] != "#":
            if s[i] != ",":
                curr_len += s[i]
            else:
                lengths.append(int(curr_len))
                curr_len = ""
            i += 1
        
        # At this point i will be at "#"'s index
        # We should advance it one more time to start extracting the words
        i += 1
        for length in lengths:
            word = s[i:i+length]
            res.append(word)
            i = i + length

        return res