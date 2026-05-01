class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, left, right = 0, 0, 0
        seen_chars = set()

        while right < len(s):
            # Grow our window
            if s[right] not in seen_chars:
                seen_chars.add(s[right])
                res = max(res, len(seen_chars))
            # Shrink until valid
            else:
                while s[right] != s[left]:
                    # Remove the char from the set
                    seen_chars.remove(s[left])
                    left += 1
                
                # At this point left is at the same char as right
                left += 1 # Advance it one more time


            # The right pointer will always move forward
            right += 1

        return res