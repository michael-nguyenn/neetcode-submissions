# n cannot be bigger than m 

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # maintain three pointers and fill from the back
        cur = m + n - 1
        first, second = m - 1, n - 1

        # loop for the entire size of n
        while second >= 0:
            if first >= 0 and nums1[first] > nums2[second]:
                nums1[cur] = nums1[first]
                first -= 1
            else:
                nums1[cur] = nums2[second]
                second -= 1
            
            cur -= 1



        


        
        