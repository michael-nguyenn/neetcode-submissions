class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res, left, counts = 0, 0, {}

        for right in range(len(s)):
            # Add the character to the frequencies
            counts[s[right]] = 1 + counts.get(s[right], 0)

            win_len = right - left + 1

            # Then we'll make sure the window is valid
            if win_len - max(counts.values()) > k:
                # Remove what's at left pointer
                counts[s[left]] -= 1

                # Move the left pointer
                left += 1
            
            # Recalculate win_len after potential left pointer movement
            win_len = right - left + 1

            # Then we'll see if the current window is the largest
            res = max(win_len, res)

        return res