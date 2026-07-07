class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_counts = { 0 : 1}
        prefix_sum, res = 0, 0

        for num in nums:
            prefix_sum += num
            diff = prefix_sum - k

            if diff in prefix_counts:
                res += prefix_counts[diff]
            
            # then we update
            prefix_counts[prefix_sum] = 1 + prefix_counts.get(prefix_sum, 0)
        
        return res
