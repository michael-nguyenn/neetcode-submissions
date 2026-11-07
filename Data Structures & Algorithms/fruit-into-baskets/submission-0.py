"""
Problem
- fruits[i] = type of fruit in ith position
- 2 baskets, each basket only holding one type of fruit
- starting from any tree, you pick one fruit from every tree while moving -> until you can't fit anymore.
    - contiguous section of array where there is at most two types of fruit

Strategy - Brute Force
- For index in fruits, we can attempt to fill out as much as possible 
- this would be O(n^2)

Example [0,1,2,2]
- index 0, we put 0 in our first basket, then we put 1 in our basket, then we see 2, so we stop
- index 1, we put 1, then we put 2, then we put 2 = 3
- index 2, we put 2, then we put 2  = 2
- index 3, we put 2 and we're at the end = 1

Example [1,2,3,2,2]
- index 0, we put 1, then we put 2
- index 1 we put 2 then we put 3, then 2, then 2 = 4
- index 2 we put 3 then two , then two = 3
- index 3 = 2
- index 4 = 1

Strategy Sliding Window
- A window is valid once you have exactly two types of fruit (r pointer)
- A window is invalid when there is three types of fruit (l pointer)
- We can track the frequencies of our window, adding to it {fruit:count}
- Once our window has more than two types, we must shrink from the left until there is exactly one type left 
- This gives a O(n) complexity vs n^2

Example [1,1,2,3,2,2]
- {1:2, 2:1}
- we hit a 3 and see that our window is full, so then we shrink the left ptr until there is just one key left
- {2:1}, now we can add 3 {2:1, 3:1}

"""

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res, freqs = 0, {}
        l = 0
        for r in range(len(fruits)):
            # Have to make sure our window is valid
            while fruits[r] not in freqs and len(freqs.keys()) == 2:
                # remove from l ptr until there is only one type of fruit
                freqs[fruits[l]] -= 1
                if freqs[fruits[l]] == 0:
                    del freqs[fruits[l]]
                    l += 1
                    break

                l += 1
            
            # add the fruit to our window
            freqs[fruits[r]] = 1 + freqs.get(fruits[r], 0)
            res = max(res, sum(freqs.values())) # O(1) since freqs holds at most 2
        
        return res


        