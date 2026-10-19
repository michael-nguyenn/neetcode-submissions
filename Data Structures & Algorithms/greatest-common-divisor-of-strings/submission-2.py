import math 

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        n1 = len(str1)
        n2 = len(str2) 

        # Check if sets are same 
        if set(str1) != set(str2):
            return ""

        # Max length of substring has to be a gcd of the char 
        gcd = math.gcd(n1,n2)
        return str1[:gcd]