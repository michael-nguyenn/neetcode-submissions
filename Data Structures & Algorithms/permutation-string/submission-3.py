class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_map = {}
        s2_map = {}
        
        # Build Hash Map
        for i in range(len(s1)):
            s1_map[s1[i]] = 1 + s1_map.get(s1[i], 0)
        
        for i in range(len(s2)):
            # need to remove previous entry
            if i >= len(s1):
                to_remove = i - len(s1)
                s2_map[s2[to_remove]] -= 1
                if s2_map[s2[to_remove]] == 0:
                    del s2_map[s2[to_remove]]
                
            # then add current entry
            s2_map[s2[i]] = 1 + s2_map.get(s2[i], 0)

            if s1_map == s2_map:
                return True
        
        return False
