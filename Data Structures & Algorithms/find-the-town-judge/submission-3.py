class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people = {i: {'trusted': 0, 'trusts': 0} for i in range(1, n+1)}

        for person, t in trust:
            people[t]['trusted'] += 1
            people[person]['trusts'] += 1
            
        for person, counts in people.items():
            if counts['trusted'] == n-1 and counts['trusts'] == 0:
                return person
        
        return -1
        