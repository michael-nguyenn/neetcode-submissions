class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs: return ""

        res = ""

        for string in strs:
            res += str(len(string)) + "#" + string

        return res

    def decode(self, s: str) -> List[str]:
        if not s: return []

        res = []

        i = 0
        while i < len(s):
            cur_len_str = ""
            while s[i] != "#":
                cur_len_str += s[i]
                i += 1
            
            # index is currently at #
            i += 1
            slice_amount = int(cur_len_str)
            res.append(s[i : i + slice_amount])

            i += slice_amount
        
        return res

