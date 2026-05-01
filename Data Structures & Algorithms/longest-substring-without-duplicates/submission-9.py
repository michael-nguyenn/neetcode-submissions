class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            seen_chars = set()
            cur_len = 0
            for j in range(i, len(s)):
                if s[j] not in seen_chars:
                    cur_len += 1
                    seen_chars.add(s[j])
                else:
                    break
                
                res = max(res, cur_len)

        return res


                