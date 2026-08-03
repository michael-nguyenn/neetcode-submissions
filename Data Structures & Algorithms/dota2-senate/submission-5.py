class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = [x for x in senate]

        # Brute Force method: simulate whole thing
        n = len(senate)

        members = {'D':0,'R':0}
        members['D'] = senate.count('D')
        members['R'] = senate.count('R')

        i = 0
        queue = [senate[0]]
        while members.get('D') > 0 and members.get('R') > 0: 
            i = (i+1) % n
            member = senate[i]
            if member == 'X':
                continue

            if not queue:
                queue.append(member)
                continue

            if queue[-1] == member:
                queue.append(member)
                continue

            queue.pop()
            senate[i] = 'X'
            members[member] -= 1
            #print(senate)

        if members.get('D') > 0: 
            return 'Dire'

        if members.get('R') > 0:
            return 'Radiant'