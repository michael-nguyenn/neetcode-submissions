class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cur_substr, res = "", ""
        counts, w_counts = {}, {}

        # First loop is to count the frequencies of t
        for c in t:
            counts[c] = 1 + counts.get(c, 0)        
        
        left = 0
        need = len(counts)  # how many distinct chars we need to satisfy
        have = 0 # how many distinct characters are satisfied
        for right in range(len(s)):
            # Only care for relevant characters
            if s[right] in counts:
                w_counts[s[right]] = 1 + w_counts.get(s[right], 0)

                if w_counts[s[right]] == counts[s[right]]:
                    have += 1
            

            while have == need:
                # So now if our window is valid we will shrink
                res = s[left:right+1] if res == "" or (right - left + 1) <= len(res) else res
                
                if s[left] not in counts:
                    left += 1
                elif w_counts[s[left]] > counts[s[left]]:
                    w_counts[s[left]] -= 1
                    left += 1
                else:
                    have -= 1
                    w_counts[s[left]] -= 1
                    left += 1

        return res