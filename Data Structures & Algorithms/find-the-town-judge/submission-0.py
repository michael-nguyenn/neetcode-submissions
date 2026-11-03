"""
Strategy
- n = 4
- HashMap towns person -> trusted (needs to be n-1 len)
- HashMap person -> trusts
"""

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people = {}

        for person, trust in trust:
            if trust not in people:
                people[trust] = {'trusted': set(), 'trusts': set()}
            if person not in people:
                people[person] = {'trusted': set(), 'trusts': set()}
            
            people[trust]['trusted'].add(person)
            people[person]['trusts'].add(trust)
            
        for person, sets in people.items():
            if len(sets['trusted']) == n-1 and len(sets['trusts']) == 0:
                return person
        
        return -1
            
        