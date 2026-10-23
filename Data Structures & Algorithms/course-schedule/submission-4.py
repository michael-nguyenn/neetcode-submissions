"""
Problem
- Given a list of prerequisites, have to determine if we can finish all the courses

Idea
- Build a graph where edge a -> b means that b is a prereq for a
- If we can go through each course and traverse them without running into a cycle then we have legal a legal course schedule

Strategy
- Build an adjacency list 
- From each course, we do a dfs until there is no prereqs anymore. That means this course is legal.
- Once we head down through a path once, we don't have to do it again since it's already marked safe
- As we head down a path, if the node doesn't exist yet we create the entry and mark it false. If we make it all the way down we can then mark it true
- If the node exists in visited, it means we've already visited and there is a cycle

Example
adj = {0: [2, 3], 1: [0], 2: [], 3: [1]}
visited = {0:False, 2:True, 3:False, 1:False}

- 0, has two prereqs, 2/3 calls on 2
- 2 is not in visited, adds itself as False, has no children changes to True
- Returns to 0 then calls 3
- 3 is not in visited, adds itself as False, has one child 1, calls 1
- 1 adds itself to the path sees 0 is in and not set to True and gg we're done
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj[prereq].append(course)
        
        visited = set()
        def dfs(course):
            # double duty as a visited and a cache
            if course in visited:
                return False
            
            # otherwise add it to the set starting false
            visited.add(course)

            # then go thru children and check
            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
            
            visited.remove(course)
            adj[course] = []
            return True

        # Do dfs on every course, if we can make it to the end, then it's legal
        for course in range(numCourses):
            print(course)
            if not dfs(course):
                return False
        
        return True
        