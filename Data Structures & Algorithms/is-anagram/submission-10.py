class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_list = list(s)
        t_list = list(t)

        s_list.sort()
        t_list.sort()

        return s_list == t_list


        
        