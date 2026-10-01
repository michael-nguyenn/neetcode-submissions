class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        res = []
        last_idx = {} # char -> last_idx 
        
        for i, char in enumerate(s):
            last_idx[char] = i

        # go char by char and fill up the partition
        count, end = 0, 0
        for i, char in enumerate(s):
            count += 1
            end = max(end, last_idx[char]) # keeps on updating

            if i == end:
                res.append(count)
                count = 0
                end = 0 # this gets reassigned anyway

        return res
                




        