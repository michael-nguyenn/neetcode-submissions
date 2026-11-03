class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people = {i: 0 for i in range(1, n+1)}

        for person, t in trust:
            people[t] += 1
            people[person] -= 1
            
        for person, counts in people.items():
            if counts == n-1:
                return person
        
        return -1
        