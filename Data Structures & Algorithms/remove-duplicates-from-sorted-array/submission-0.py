class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
         # Track the number of unique elements
        k = 0
        i = 0
        # Track the end of the new array
        length = len(nums)

        # Loop from beginning to end
        while i < length:

            # Increment k
            k = k + 1

            # In the case of a dupe, we should count the dupes
            dupes = 0

            # If i is same as i + 1, then we should count the # of dupes
            while ((i + dupes + 1 < length) and 
                    (nums[i] == nums[i + dupes + 1])):
                # Increment the dupe counter
                dupes = dupes + 1
                # If the last element is a dupe
                print(dupes)

            if (dupes > 0):
                if nums[i] == nums[length - 1]:
                    for j in range(i + 1 + dupes, length):
                        nums[j] = None

                # Shift all other elements to the left by dupe amount
                for j in range(i + 1 + dupes, length):
                    nums[j - dupes] = nums[j]
                    nums[j] = None 

            length = length - dupes
            i = i + 1

        # Return k
        return k