class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people = {}

        for person, trust in trust:
            if trust not in people:
                people[trust] = {'trusted': 0, 'trusts': 0}
            if person not in people:
                people[person] = {'trusted': 0, 'trusts': 0}
            
            people[trust]['trusted'] += 1
            people[person]['trusts'] += 1
            
        for person, sets in people.items():
            if sets['trusted'] == n-1 and sets['trusts'] == 0:
                return person
        
        return -1
        