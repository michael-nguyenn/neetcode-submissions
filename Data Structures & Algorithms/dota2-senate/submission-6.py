from collections import deque

class Solution:

    # Use two queues, each tracking the index representing a senator's turn
    # Afterwards we'll continue until one queue is empty, the empty q signifies that party is out of senators
    # Deq from both queues, the side with the lower index means they'll ban the other senator
    # The lower indexed senator will re-enter the queue with their turn adjusted (+ len(senate))
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        n = len(senate)
        radiant, dire = deque(), deque()

        for i in range(len(senate)):
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()

            if r < d:
                radiant.append(r + n)
            else:
                dire.append(d + n)
        
        return "Radiant" if radiant else "Dire"

        