"""
Problem
- given a string s of lower case chars
- re-arrange s so that duplicates are not next to one another

Strategy
- So the hardest character to place is the most frequently occuring character
- It's impossible to form a valid string if the frequency is > len(rest) + 1
    - cccd, c:3, rest is 1 
- Otherwise we use a max heap to store (freq, char)
- While the heap still has entries
    - pop from the heap, append the char to res, decrement count
    - if count is > 0, then we can store it in temp since we can't use it next round
    - only re-add temp the next round if there is something to add
"""
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        res = []
        freqs = {}
        for char in s:
            freqs[char] = 1 + freqs.get(char, 0)

        # edge case for impossible strings
        max_freq = max(freqs.values())
        if max_freq > len(s) - max_freq + 1:
            return ""
        
        h = [(-count, char) for char, count in freqs.items()]
        heapq.heapify(h)

        temp = None
        while h:            
            count, char = heapq.heappop(h)
            res.append(char)

            if temp is not None:
                heapq.heappush(h, temp)

            temp = (count+1, char) if count+1 < 0 else None
        
        return "".join(res)