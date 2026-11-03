class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people = {}

        for person, t in trust:
            if t not in people:
                people[t] = {'trusted': 0, 'trusts': 0}
            if person not in people:
                people[person] = {'trusted': 0, 'trusts': 0}
            
            people[t]['trusted'] += 1
            people[person]['trusts'] += 1
            
        for person, counts in people.items():
            if counts['trusted'] == n-1 and counts['trusts'] == 0:
                return person
        
        return -1
        