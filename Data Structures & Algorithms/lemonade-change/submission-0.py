"""
Problem
- Sell lemonade for 5$, see if you can provide change to everyone
- Accepts 5, 10 20 bills 
- Start out with no change

Example [5, 10, 5, 5, 20]
- 5 needs no change => increase num 5s you own
- 10 needs at least a 5 => decrease 5, increase 10
- 5, 5 => increase 5s
- 20 needs either
    - 3 5 dollar bills or
    - 1 10$ and 5$

Plan
- Go through each bill
    - if 5$ -> ++5sbucket 
    - if 10$
        - check if >= 1 5$ exists and increment changes[1], --changes[0]
        - otherwise return false
    - if 20$
        - check if either >= 1 10$ and >= 1 5$ or >= 3 5$s
"""

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        # Initiate a change bucket representing 5,10,20 owned
        changes = [0] * 3

        for bill in bills:
            if bill == 5:
                changes[0] += 1
            elif bill == 10:
                if changes[0] >= 1:
                    changes[0] -= 1
                    changes[1] += 1
                else:
                    return False
            # bill == 20
            else:
                if changes[1] >= 1 and changes[0] >= 1:
                    changes[1] -= 1
                    changes[0] -= 1
                    changes[2] += 1
                elif changes[0] >= 3:
                    changes[0] -= 3
                    changes[2] += 1
                else:
                    return False
        
        return True
        