class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        adj = {n:[] for n in range(numCourses)}
        visit = set()

        # guild our adj list
        for course, pre in prerequisites:
            adj[course].append(pre)

        def dfs(course):
            if course in visit:
                return False
            
            if len(adj[course]) == 0:
                res.append(course)
                visit.add(course)
                return True
            
            visit.add(course)

            # otherwise go through the children
            for pre in adj[course]:
                if pre in res:
                    continue
                
                if not dfs(pre):
                    return False
            
            # making it here means we've cleared the prereqs
            res.append(course)
            return True


        for course in adj:
            if course not in res:
                if not dfs(course):
                    return []

        return res