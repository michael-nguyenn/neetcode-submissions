class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create an adj list mapping courses to their prereqs
        pre_map = { i:[] for i in range(numCourses) }
        
        # fill up the adj list
        for course, pre in prerequisites:
            pre_map[course].append(pre)

        visited = set() # holds courses along current path

        def dfs(course):
            if course in visited:
                return False
            
            if len(pre_map[course]) == 0:
                return True
            
            # Otherwise add it to visited and explore all prereqs
            visited.add(course)
            for pre in pre_map[course]:
                if not dfs(pre):
                    return False

            # Making it here means that we can take this course
            visited.remove(course)
            pre_map[course] = []
            return True

        # We have to still loop through all our courses b/c
        # some may be disconnected
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True