from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {}
        for course,pre in prerequisites: 
            graph[course] = graph.get(course,set())
            graph[course].add(pre)
        
        q = deque(range(numCourses))
        taken = set()
        while q: 
            n = len(q)
            for _ in range(n):
                next_flag = 0
                course = q.popleft() 
                pres = graph.get(course,None)
                if not pres: 
                    taken.add(course)
                    continue
                
                for pre in pres: 
                    if pre not in taken: 
                        q.append(course)
                        next_flag = 1
                        break

                if next_flag == 1:
                    continue

                taken.add(course)
            
            if n == len(q): 
                return False

        return True