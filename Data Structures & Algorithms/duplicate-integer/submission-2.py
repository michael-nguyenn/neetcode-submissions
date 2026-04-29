class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # HashMap to hold numbers
        numbers = {}

        # Loop through each number in our list
        for n in nums:
            if n in numbers:
                return True
            else:
                numbers.setdefault(n, 1)

        return False