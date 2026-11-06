"""
Problem
- spell + potion is good if their product is >= success
- for each spell, see how many potions, are success

Example
- spell[0] = 2, 2x2, 2x3 2x6
- spell[1] = 5, 5x2, 5x3, 5x6
- spell[2] = 1, 1x2, 1x3, 1x6
- for each spell, multiple out each of the potions -> O(n^2)

- for each potion, calculate the min spell dmg needed to be success
- 2: 10/2 = 5
- 3: 10/3 = 3.33 
- 6: 10/6 = 1.16
- O(n)

- 
"""

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = [0 for _ in range(len(spells))] 
        cache = {} # spell -> how many success

        for i, spell in enumerate(spells):
            if spell in cache:
                res[i] = cache[spell]
                continue

            for potion in potions:
                if spell * potion >= success:
                    res[i] += 1
            
            cache[spell] = res[i]

        return res
