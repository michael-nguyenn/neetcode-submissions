class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cur_substr, res = "", ""
        counts, w_counts = {}, {}

        # First loop is to count the frequencies of t
        for c in t:
            counts[c] = 1 + counts.get(c, 0)        
        
        left = 0
        for right in range(len(s)):
            
            # Only care for relevant characters
            if s[right] in counts:
                w_counts[s[right]] = 1 + w_counts.get(s[right], 0)
            
            # Build the substring
            cur_substr += s[right]

            while True:
                valid = True
                for k in counts:
                    # If the value of k is less than in counts
                    # then our window isn't valid yet
                    if w_counts.get(k, 0) < counts[k]:
                        valid = False
                        break
                
                if not valid: break
                
                # So now if our window is valid we will shrink
                if res == "":
                    res = cur_substr

                res = cur_substr if len(cur_substr) <= len(res) else res

                if s[left] not in counts:
                    cur_substr = cur_substr[1:]
                    left += 1
                elif w_counts[s[left]] > counts[s[left]]:
                    w_counts[s[left]] -= 1
                    cur_substr = cur_substr[1:]
                    left += 1
                else:
                    break
            
        return res