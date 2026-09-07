from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        res = math.inf
        min_costs = [math.inf] * n
        min_costs[src] = 0

        # Build Adjacent List for traversal
        adj_list = {i:[] for i in range(n)}

        for (s, d, cost) in flights:
            adj_list[s].append((d,cost))

        # Load up our q for BFS
        q = deque()

        for flight in adj_list[src]:
            d, cost = flight
            min_costs[d] = cost
            q.append((d, cost))
        
        while k >= 0 and q:
            for _ in range(len(q)):
                d, cost = q.popleft()
                
                if d == dst:
                    res = min(res, cost)
                
                for flight in adj_list[d]:
                    new_cost = flight[1] + cost
                    if new_cost < min_costs[flight[0]]: 
                        q.append((flight[0], new_cost))
                        min_costs[flight[0]] = new_cost
            
            k -= 1
        
        return -1 if res == math.inf else res