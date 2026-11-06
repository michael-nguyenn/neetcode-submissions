"""
Problem
- two strings, return shortest substring of s that contains t

Strategy
- create a map of t counts 
- start a window and expand it right adding characters to a s map
- once the window is the same as t, shrink it from the left until it isn't valid anymore
- keep track of the size of the valid windows to see what your best result is

- we can reduce some complexity by creating a map of t {x:1, y:1, z:1}
- also create a map of s {}
   0123456789
- "OUZODYXAZV"
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_map, t_map = {}, {}
        start, end = 0, 0
        shortest = float('inf')

        for char in t:
            t_map[char] = 1 + t_map.get(char, 0)
        
        need = len(t_map)  # how many distinct chars we need to satisfy
        have = 0 # how many distinct characters are satisfied
        
        left = 0
        for right in range(len(s)):
            # if the char is in t_map, add it
            if s[right] in t_map:
                s_map[s[right]] = 1 + s_map.get(s[right], 0)

                if s_map[s[right]] == t_map[s[right]]:
                    have += 1

            while have == need:
                window_size = right - left + 1
                if window_size < shortest:
                    shortest = window_size
                    start, end = left, right
                
                # for shrink, if the char at left is in map then remove
                if s[left] in t_map:
                    if s_map[s[left]] > t_map[s[left]]:
                        s_map[s[left]] -= 1
                    elif s_map[s[left]] == t_map[s[left]]:
                        s_map[s[left]] -= 1
                        have -= 1
                
                left += 1
    
        # now we can return the string
        return s[start:end+1] if shortest < float('inf') else ""


        