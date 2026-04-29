class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        # an array of arrays (nums + 1) because frequencies can range from 1 - len(nums) inclusive
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in counts.items():
            # index of buckets represents the frequencies
            buckets[freq].append(num)

        res = []
        for i in range(len(buckets) - 1, 0, - 1):
            while len(buckets[i]) > 0:
                res.append(buckets[i].pop())
                if len(res) == k:
                    break
            
            if len(res) == k:
                break
        
        return res