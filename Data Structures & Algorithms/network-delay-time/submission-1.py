from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj_list = defaultdict(list)
        for src, dst, weight in times:
            adj_list[src].append((dst, weight))

        path_cost = {i : float('inf') for i in range(1, n + 1)}

        def dfs(node: int, total: int) -> None:
            if total >= path_cost[node]:
                return

            path_cost[node] = total

            for neigh, cost in adj_list[node]:
                dfs(neigh, total + cost)
        
        dfs(k, 0)
        res = max(path_cost.values())
        return -1 if res == float('inf') else res
