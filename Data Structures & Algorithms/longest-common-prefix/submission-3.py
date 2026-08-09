class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ""

        cur_idx = 0
        cur_char = ""
        while True:
            for i in range(len(strs)):
                if not strs[i] or cur_idx == len(strs[i]):
                    return longest_prefix

                if i == 0:
                    cur_char = strs[i][cur_idx]
                    continue
                elif strs[i][cur_idx] != cur_char:
                    return longest_prefix
                
            longest_prefix += cur_char
            cur_idx += 1
            print(longest_prefix)

