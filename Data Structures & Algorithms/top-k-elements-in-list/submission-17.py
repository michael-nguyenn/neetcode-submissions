"""
Problem
- Given an array of size n, must return the k most frequent elements
- array size n, means n is the highest frequency

Strategy
- We can create an array of n+1 buckets O(n) time and space
- Then we go nums, and create a hash map mapping, num to frequency
- Then we go through each key, value of the hash map, and fill in the bucket
- Then go through the buckets backwards and grab the k most frequent elements

Cases
- k will be less than the # of distinct elements in nums so that means our final loop will always run to completion
- There will be at least one element 
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        buckets = [[] for _ in range(len(nums)+1)]
        freqs = {}

        # fill out the frequency map
        for num in nums:
            freqs[num] = 1 + freqs.get(num, 0)

        # fill out our frequency buckets
        for num, freq in freqs.items():
            buckets[freq].append(num)

        # get the k most frequently occuring 
        for i in range(len(buckets)-1, -1, -1):
            if buckets[i]:
                for num in buckets[i]:
                    res.append(num)
                    if len(res) == k:
                        return res

        

        