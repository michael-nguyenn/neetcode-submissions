class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        n = len(numbers)

        def binary_search(t, left): 
            
            if not numbers:
                return None

            right = len(numbers) - 1
            
            while left <= right: 
                mid = (left + right) // 2
                if numbers[mid] == t:
                    return mid 
                
                if numbers[mid] < t: 
                    left = mid + 1
                else:
                    right = mid - 1
                
            return None 

        for i in range(n): 
            num = numbers[i]
            contra = target - num 
            idx = binary_search(contra,i+1)

            if idx: 
                return [i + 1, idx + 1]

        return [None,None]
        