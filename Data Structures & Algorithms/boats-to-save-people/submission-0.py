"""
Problem
- people[i] = weight of ith person
- have infinite boats
- Each boat carries at most two people, provided sum of weight is <= limit
- find minimum number of boats to carry everyone

Example
- [1,2,4,6,7,10]
Strategy
- can we sort people? [1,2,2,3,3]
- start the left and right pointers at either ends of the array
- if left+right <= limit, then we can move each pointer
- if left+right > limit, then we only move the right
- this works because if we couldn't form a valid pairing between the largest and the smallest, then it's impossible to form between largest and second smallest, etc
- everytime we move a pointer, it means one extra boat
- this loop will run as long as left < right
"""

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people)-1
        res = 0
        while left <= right:
            if people[right] + people[left] <= limit:
                left, right = left+1, right-1
            else:
                right -= 1
            
            res += 1
        
        return res
        