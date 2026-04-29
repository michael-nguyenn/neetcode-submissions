class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            # This pattern allows us to increment without worrying 
            # If the key exists or not
            counts[num] = 1 + counts.get(num, 0)

        temp = []
        for num, count in counts.items():
            temp.append((count, num))
        
        temp.sort()

        res = []
        for i in range(k):
            res.append(temp.pop()[1])

        return res
