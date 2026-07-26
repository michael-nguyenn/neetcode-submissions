class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []

        for i in range(len(temperatures)):
            j = i
            days = 0

            while j + 1 < len(temperatures) and temperatures[j + 1] <= temperatures[i]:
                j+= 1
                days += 1

            if j + 1 < len(temperatures) and temperatures[j + 1] > temperatures[i]:
                days += 1
            else:
                days = 0
            
            res.append(days)

        return res