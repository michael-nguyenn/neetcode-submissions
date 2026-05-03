class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts, res = {}, ""

        # Frequency map
        for letter in t:
            counts[letter] = 1 + counts.get(letter, 0)

        # Main Loop
        for i in range(len(s)):
            # To hold current frequencies
            cur_counts = {}
            cur_substr = ""

            for j in range(i, len(s)):
                if s[j] in counts:
                    cur_counts[s[j]] = 1 + cur_counts.get(s[j], 0)

                cur_substr += s[j]
                
                valid = True

                for k in counts:
                    if cur_counts.get(k, 0) < counts[k]:
                        valid = False
                        break
                        
                if valid:
                    print(cur_substr)

                    if res == "":
                        res = cur_substr

                    res = cur_substr if len(cur_substr) <= len(res)  else res
                    break

        
        return res
