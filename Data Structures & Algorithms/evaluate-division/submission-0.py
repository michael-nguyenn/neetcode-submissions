"""
Given a/b * b/c = a/c -> 2 * 3 = 6
- We can do a graph where node is a numerator, the edge is the division to the denominator
- a <-> b <-> c
- going backwards would be 1/division
"""

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # make the adjacency list
        adj = collections.defaultdict(list)

        for i, ops in enumerate(equations):
            op1, op2 = ops

            adj[op1].append((op2, values[i]))
            adj[op2].append((op1, 1 / values[i]))

        print(adj)

        def bfs(src, dst):
            q, visit = collections.deque(), set()
            q.append((src, 1))
            visit.add(src)

            while q:
                cur, cost = q.popleft()

                if cur == dst:
                    return cost

                for nei in adj[cur]:
                    op, val = nei
                    if op not in visit:
                        q.append((op, val * cost))
                        visit.add(op)
            
            return -1
        
        res = []
        for src, dst in queries:
            if src not in adj or dst not in adj:
                res.append(-1)
                continue

            res.append(bfs(src, dst))

        return res
        