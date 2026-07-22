import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # We first need to turn our array into an adjacency list for ez traversal
        graph_list = defaultdict(list)

        for src, dst, weight in times:
            graph_list[src].append((dst, weight))

        min_heap = [(0, k)] # weight, node
        visited = set()
        res = 0 # holds the shortest time to the last node 

        while min_heap:
            weight, src_node = heapq.heappop(min_heap)

            # If we visited a node it means it's guaranteed to be the shortest path
            if src_node in visited:
                continue

            # Now we can visit it and update res
            visited.add(src_node)
            res = weight

            # Go thru neighbors and add to our heap
            for dst_node, dst_weight in graph_list[src_node]:
                heapq.heappush(min_heap, (dst_weight + weight, dst_node))

        # if the graph was disconnected then we wouldn't visit all n nodes
        return -1 if len(visited) != n else res