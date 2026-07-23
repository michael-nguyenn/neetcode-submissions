class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):

            # determines the ith position in n is 0 or 1
            bit = (n >> i) & 1

            # slot in that bit from the end of res
            res = (bit << 31 - i) | res
        
        return res