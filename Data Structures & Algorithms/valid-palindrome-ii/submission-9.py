class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        def check(i,j,counter=0):
            if i > j: 
                return True
            if counter > 1:
                return False
            if s[i] == s[j]:
          	    return check(i+1,j-1,counter)
            
            return check(i+1,j,counter+1) or check(i, j-1,counter+1)
        
        return check(i,j,0)