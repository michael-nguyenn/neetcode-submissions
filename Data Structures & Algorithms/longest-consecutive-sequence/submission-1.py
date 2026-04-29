class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_sequence = 0
        nums = set(nums)

        for num in nums:
            if num - 1 in nums:
                continue
            else:
                # num is currently the start of a sequence
                sequence_num = num
                cur_seq_len = 1
                while sequence_num + 1 in nums:
                    cur_seq_len += 1
                    sequence_num += 1
                
                longest_sequence = max(cur_seq_len, longest_sequence)

        return longest_sequence

