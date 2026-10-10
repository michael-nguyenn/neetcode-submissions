"""
Problem
- Take an integer, split them into their digits, and then sum their squares
- You keep on doing that ^ until you either reach 1, or you reach a duplicate

Cases
- Is it any duplicate counts as a non happy number? I believe so

Strat
- Create a set holding the result from each round
- In each round
    - Convert the integer to a string
    - Go through each digit in the string, convert it to an int, and sum it up
    - Check if the sum equals 1, if so return true
    - Check if sum is already in our set -> return false
    - Add the sum to our set, and reset the num for next round
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        n_string = str(n)
        
        while True:
            squared_sum = 0
            for char in n_string:
                squared_sum += int(char)**2
            
            if squared_sum == 1:
                return True
            if squared_sum in visited:
                return False
            
            visited.add(squared_sum)
            n_string = str(squared_sum)
        