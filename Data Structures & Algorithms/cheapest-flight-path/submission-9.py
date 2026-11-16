import math

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    
        f_map = {}
        for from_, to, price in flights: 
            f_map[from_] = f_map.get(from_,[])
            f_map[from_].append((to,price))

        memo = {} 
        def dfs(i,stops=0):

            if i == dst: 
                return 0
            
            if stops >= k+1:
                return math.inf

            if (i,stops) in memo:
                return memo.get((i,stops))
            
            cheapest = math.inf
            for to, price in f_map.get(i,[]): 
                cheapest = min(cheapest,price+dfs(to,stops+1))
            
            memo[(i, stops)] = cheapest
                
            return cheapest
            
        low = dfs(src,0)

        return -1 if low == math.inf else low
        