"""
- Sort the potions first O(nlogn)
- Then for each spell, we calculate the right most potion that allows us to be successful

Strategy
- left and right on potions
- get mid
- if spell[i] * potion[mid] < success, we need to search right
- if spell[i] * potion[mid] >= success, we need to search left
- after we find that then every spell from left -> end is our answer
"""

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        cache = {} # spell -> success_count
        res = [0 for _ in range(len(spells))]
        
        for i, spell in enumerate(spells):
            if spell in cache:
                res[i] = cache[spell]
                continue

            left, right = 0, len(potions) - 1
            smallest = len(potions)
            while left <= right:
                mid = (left + right) // 2

                if spell * potions[mid] >= success:
                    smallest = mid
                    right = mid - 1
                else:
                    left = mid + 1
             
            res[i] = len(potions) - smallest
            cache[spell] = res[i]

        return res


