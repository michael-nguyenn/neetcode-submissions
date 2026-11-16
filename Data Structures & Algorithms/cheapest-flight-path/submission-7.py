"""
Problem
- Airports labeled 0 - (n-1)
- Flights that represent a one way weighted edge from airport to airport

Strategy
- Build an adjacency list of flights and their edges
- We can use a heap to store the cheapest flight and run rounds up to k times
"""
from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i:[] for i in range(n)}
        q = deque()
        cheapest = [float("infinity") for i in range(n)]

        for s, d, cost in flights:
            adj[s].append((d,cost))
        
        # from the adj list we can seed
        q.append((src, 0))
        
        # then we run the loop until k+1 (0,1)
        for _ in range(k+1):
            # capture the level of the heap
            for _ in range(len(q)):
                # pop the heap
                cur, cost = q.popleft()

                # go thru the children, and add their children + cost to q
                for (d, c) in adj[cur]:
                    if cost+c < cheapest[d]:
                        cheapest[d] = cost+c
                        q.append((d, cost+c))

        return cheapest[dst] if cheapest[dst] < float("infinity") else -1

        