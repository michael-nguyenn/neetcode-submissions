"""
Problem
- target string 0000, each of index of the string represents 0-9, and there is exactly one combination to open the lock, we can % 10 to make sure it wraps
- deadends shows a combination that we cannot reach (we cannot progress from there)
- need to return the minimum total number of turns to open or -1
- one turn is one wheel turnng once

Strategy
- From any position on your wheel you can move forward or backwards. That means starting at 0000, we can move to 8 possible combinations
    - 1000, 9000, 0100, 0900, 0010, 0090, 0001, 0009
- So from our starting position, we can move each index in cur_comb 8 ways
- We will BFS from 0000, and count the rounds until target or until the q is empty
- If adding the combination hits a deadend, then we do not append it 

"""
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
            
        q, visited = deque(["0000"]), set(["0000"])
        
        rounds = 0
        while q:
            for _ in range(len(q)):
                cur_comb = q.popleft()
                
                if cur_comb == target:
                    return rounds
                
                cur_comb = list(cur_comb)
                for i in range(len(cur_comb)):
                    copy1 = cur_comb.copy()
                    copy2 = cur_comb.copy()
                    cur_dig = int(cur_comb[i])
                    copy1[i] = str((cur_dig + 1) % 10)
                    copy1 = "".join(copy1)
                    if copy1 not in deadends and copy1 not in visited:
                        q.append(copy1)
                        visited. add(copy1)

                    copy2[i] = str((cur_dig - 1) % 10)
                    copy2 = "".join(copy2)
                    if copy2 not in deadends and copy2 not in visited:
                        q.append(copy2)
                        visited.add(copy2)
            rounds += 1
        
        return -1
   
                    
                                       

        
        